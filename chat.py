#!/usr/bin/env python
import os
import ipdb
from llama_index import (
        VectorStoreIndex,
        SimpleDirectoryReader,
        StorageContext,
        load_index_from_storage,
)
from llama_index.memory import ChatMemoryBuffer


def main():
    index = build_index()

    # Query only
    # query_engine = index.as_query_engine()
    # resp = query_engine.query("study of government")
    # print(resp)

    # Full chat
    memory = ChatMemoryBuffer.from_defaults(token_limit=3000)
    chat_engine = index.as_chat_engine(memory=memory)

    while True:
        q = getinput()
        if not q:
            break
        streaming_response = chat_engine.stream_chat(q)
        for token in streaming_response.response_gen:
            print(token, end="")


def getinput():
    while True:
        try:
            q = input("\n>> ")
            if q == "q":
                return False
            elif not q:
                continue
            return q
        except EOFError:
            return False


def build_index():
    if os.path.exists("usecache"):
        print("using cache")
        storage_context = StorageContext.from_defaults(persist_dir='./storage')
        index = load_index_from_storage(storage_context)
    else:
        print("not using cache")
        confirm = input("confirm (y/n): ")
        if confirm != "y":
            print("abort")
            return
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist()
        with open("usecache", "w") as f:
            pass
    return index


main()
