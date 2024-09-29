from modules.assistant import Assistant
import tiktoken

class Translator:
    def __init__(self, assistant_id):
        self.assistant_id = assistant_id
        self.assistant = Assistant()

    def translate_text(
        self,
        text,
        source_language='Detect Language',
        target_language='English',
        model_name='gpt-4o-mini',
        progress_callback=None
    ):
        # Initialize the tokenizer for the specified model
        enc = tiktoken.encoding_for_model(model_name)

        # Tokenize the text
        tokens = enc.encode(text)
        max_tokens_per_chunk = 2048  # Adjust based on model's max input tokens

        # Split tokens into chunks
        chunks = [
            tokens[i:i + max_tokens_per_chunk]
            for i in range(0, len(tokens), max_tokens_per_chunk)
        ]

        translated_text = ""
        total_chunks = len(chunks)

        for index, chunk in enumerate(chunks):
            chunk_text = enc.decode(chunk)
            prompt = self._build_prompt(
                chunk_text, source_language, target_language
            )
            response = self.assistant.chat_with_assistant(
                self.assistant_id, prompt, model_name
            )
            translated_text += response + "\n"

            # Update progress
            if progress_callback:
                progress = (index + 1) / total_chunks
                progress_callback(progress)

        return translated_text

    def _build_prompt(self, text, source_language, target_language):
        instruction = (
            "NEVER PROVIDE YOUR OWN INPUT. "
            "ONLY RESPOND WITH THE RAW, TRANSLATED TEXT "
            "IN THE EXACT FORMAT AS YOU RECEIVE IT!"
        )
        if source_language == 'Detect Language':
            prompt = f"{instruction} Translate the following text to {target_language}:\n\n{text}"
        else:
            prompt = f"{instruction} Translate the following text from {source_language} to {target_language}:\n\n{text}"
        return prompt
