package de.bodemann.fraktur

import android.app.Application
import android.content.ClipData
import android.content.ClipboardManager
import androidx.core.content.getSystemService
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

class FrakturViewModel(application: Application) : AndroidViewModel(application) {
    private val _fraktures: MutableStateFlow<List<String>> = MutableStateFlow(listOf<String>())
    val fraktures: StateFlow<List<String>> = _fraktures.asStateFlow()

    private val _error: MutableStateFlow<String?> = MutableStateFlow<String?>(null)
    val error: StateFlow<String?> = _error.asStateFlow()

    private val _loading: MutableStateFlow<Boolean> = MutableStateFlow(false)
    val loading: StateFlow<Boolean> = _loading.asStateFlow()

    private val pythonBackend = PythonBackend()
    private val pythonDirectly = PythonDirectly(application.applicationContext)

    private var requestFraktures: suspend (message: String) -> List<String> = pythonBackend::requestFraktures

    private val _embeddedPythonMode: MutableStateFlow<Boolean> = MutableStateFlow(false)
    val embeddedPythonMode: StateFlow<Boolean> = _embeddedPythonMode.asStateFlow()

    fun loadNewFraktures(message: String) {
        _loading.update { true }
        viewModelScope.launch {
            try {
                val response = requestFraktures(message)
                _fraktures.update {
                    response
                }
            } catch (th: Throwable) {
                _error.update { th.message }
            } finally {
                _loading.update { false }
            }
        }
    }

    fun copyToClipBoard(message: String) {
        val manager = getApplication<Application>().getSystemService<ClipboardManager>()

        val clip = ClipData.newPlainText("Fraktur", message)
        manager?.setPrimaryClip(clip)
    }

    fun usePython() {
        requestFraktures = pythonDirectly::requestFraktures
        _embeddedPythonMode.update { true }
        _error.update { null }
        _fraktures.update { listOf() }
    }

    fun useWebServer() {
        requestFraktures = pythonBackend::requestFraktures
        _embeddedPythonMode.update { false }
        _error.update { null }
        _fraktures.update { listOf() }
    }
}
