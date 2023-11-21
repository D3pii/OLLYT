"""
quickly summarise a youtube video
"""
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = Ollama(
    model="llama2", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

# video id and prompt
VID_ID = "P8accXNcwjs"
proompt = "summerarize this video, negate any information about sponsors list also the apps talked about, what they replace and the notable things they offer like peer to peer and if they are FOSS : "

# prepping
api = YouTubeTranscriptApi.get_transcript(VID_ID)
TRANSSCRIPT = " ".join([row["text"] for row in api])
TEXT = proompt + TRANSSCRIPT

# write output to file
f = open("output.txt", "a", "t")
f.write(VID_ID + "\n")
f.write(llm(TEXT))
f.write("-" * 20 + "\n")
f.close()
