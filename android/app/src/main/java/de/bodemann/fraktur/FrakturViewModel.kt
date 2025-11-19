package de.bodemann.fraktur

import android.app.Application
import android.content.ClipData
import android.content.ClipboardManager
import androidx.compose.runtime.currentCompositionLocalContext
import androidx.compose.runtime.rememberCompositionContext
import androidx.compose.ui.platform.ClipEntry
import androidx.compose.ui.platform.LocalContext
import androidx.core.content.getSystemService
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.currentCoroutineContext
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

    fun requestFrakturs(message: String) {
        _loading.update { true }
        viewModelScope.launch {
            try {
                val response = pythonBackend.requestFraktures(message)
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
}
