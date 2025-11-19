package de.bodemann.fraktur

import kotlinx.serialization.json.Json
import okhttp3.MediaType.Companion.toMediaType
import retrofit2.Retrofit
import retrofit2.converter.kotlinx.serialization.asConverterFactory
import retrofit2.http.Body
import retrofit2.http.POST

interface PythonService {
    @POST("/")
    suspend fun getFraktures(
        @Body body: String
    ): List<String>
}

class PythonBackend {
    private val service = Retrofit
        .Builder()
        .baseUrl("http://localhost:5000")
        .addConverterFactory(
            Json.asConverterFactory(
                "application/json".toMediaType(),
            ),
        ).build()
        .create(PythonService::class.java)

    suspend fun requestFraktures(message: String) =
        service.getFraktures(message).map { it.removeSurrounding("\"") }
}
