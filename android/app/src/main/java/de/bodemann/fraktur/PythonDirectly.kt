package de.bodemann.fraktur

import android.content.Context
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform

class PythonDirectly(
    private val context: Context
) {
    private val python: Python by lazy {
        if (!Python.isStarted()) {
            Python.start(AndroidPlatform(context))
        }

        Python.getInstance()
    }

    suspend fun requestFraktures(message: String): List<String> {
        val converter = python.getModule("fraktur")
        val result = converter.callAttr("generate", message, "all")

        val stringResult = result.toString()
        return stringResult.split("\n")
    }
}
