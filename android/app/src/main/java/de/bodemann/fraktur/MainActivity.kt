package de.bodemann.fraktur

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.viewModels
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.defaultMinSize
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.wrapContentHeight
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.Send
import androidx.compose.material.icons.filled.Send
import androidx.compose.material3.Card
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import de.bodemann.fraktur.ui.theme.FrakturTheme

class MainActivity : ComponentActivity() {

    val vm: FrakturViewModel by viewModels()

    @OptIn(ExperimentalMaterial3Api::class)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            FrakturTheme {
                Scaffold(
                    topBar = { TopAppBar(title = { Text(text = stringResource(R.string.app_name)) }) },
                    modifier = Modifier.fillMaxSize()
                ) { innerPadding ->
                    Column(
                        modifier = Modifier.padding(innerPadding)
                    ) {
                        val fraktures by vm.fraktures.collectAsState()
                        val loading by vm.loading.collectAsState()
                        val error by vm.error.collectAsState()

                        FrakturView(
                            fraktures,
                            loading,
                            error,
                            vm::requestFrakturs,
                            vm::copyToClipBoard,
                        )
                    }
                }
            }
        }
    }
}

@Composable
fun FrakturView(
    fraktures: List<String>,
    loading: Boolean,
    error: String?,
    loadNewFraktures: (String) -> Unit,
    copyToClipboard: (String) -> Unit,
) {
    Box(
        modifier = Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        Column(
            modifier = Modifier.fillMaxSize()
        ) {
            error?.let { actualError ->
                ErrorView(actualError)
            }

            if (fraktures.isEmpty()) {
                EmptyView()
            }

            EnterMessageView(loadNewFraktures)

            FraktureListView(fraktures, copyToClipboard)
        }

        if (loading) {
            CircularProgressIndicator(
                modifier = Modifier.size(72.dp)
            )
        }
    }
}

@Composable
private fun FraktureListView(
    fraktures: List<String>,
    copyToClipboard: (String) -> Unit
) {
    LazyColumn(
        modifier = Modifier.fillMaxSize()
    ) {
        items(fraktures) { fraktur ->
            Card(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(4.dp)
                    .clickable {
                        copyToClipboard(fraktur)
                    },
            ) {
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .defaultMinSize(minHeight = 32.dp),
                    contentAlignment = Alignment.Center
                ) {
                    Text(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(vertical = 16.dp, horizontal = 8.dp),
                        textAlign = TextAlign.Center,
                        text = fraktur
                    )
                }
            }
        }
    }
}

@Composable
private fun EnterMessageView(loadNewFraktures: (String) -> Unit) {
    var tempMessage by remember { mutableStateOf("") }
    Row(
        verticalAlignment = Alignment.CenterVertically,
    ) {
        TextField(
            modifier = Modifier
                .weight(1f)
                .padding(vertical = 4.dp),
            label = { Text(stringResource(R.string.hint_fraktur)) },
            value = tempMessage,
            onValueChange = { tempMessage = it },
            trailingIcon = {
                IconButton(
                    onClick = { loadNewFraktures(tempMessage) }
                ) {
                    Icon(
                        imageVector = Icons.AutoMirrored.Filled.Send,
                        contentDescription = null
                    )
                }
            },
        )
    }
}

@Composable
private fun EmptyView() {
    Text(
        modifier = Modifier
            .fillMaxWidth()
            .background(Color.Gray.copy(alpha = 0.4f))
            .padding(16.dp),
        textAlign = TextAlign.Center,
        text = stringResource(R.string.empty)
    )
}

@Composable
private fun ErrorView(actualError: String) {
    Text(
        modifier = Modifier
            .fillMaxWidth()
            .background(Color.Red.copy(alpha = 0.4f))
            .padding(16.dp),
        textAlign = TextAlign.Center,
        text = actualError
    )
}

@Preview
@Composable
private fun FrakturViewEmpty() {
    FrakturView(
        emptyList(),
        false,
        null,
        {},
        {},
    )
}

@Preview
@Composable
private fun FrakturViewSome() {
    FrakturView(
        listOf(
            "Hello World",
            "72 101 108 108 111 32 87 111 114 108 100 ",
            "1001000 1100101 1101100 1101100 1101111 100000 1010111 1101111 1110010 1101100 1100100 ",
            "0x48 0x65 0x6C 0x6C 0x6F 0x20 0x57 0x6F 0x72 0x6C 0x64 ",
            ":alphabet-white-h::alphabet-white-e::alphabet-white-l::alphabet-white-l::alphabet-white-o:   :alphabet-white-w::alphabet-white-o::alphabet-yellow-r::alphabet-white-l::alphabet-yellow-d:",
            "Hᴇʟʟᴏ Wᴏʀʟᴅ",
            "HELLO WORLD",
        ),
        false,
        null,
        {},
        {},
    )
}

@Preview
@Composable
private fun FrakturViewLoading() {
    FrakturView(
        listOf(
        ),
        true,
        null,
        {},
        {},
    )
}

@Preview
@Composable
private fun FrakturViewError() {
    FrakturView(
        listOf(),
        true,
        "An error! Run away, protect the cats!",
        {},
        {},
    )
}
