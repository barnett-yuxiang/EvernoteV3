
### Basic

https://github.com/openai/tiktoken/tree/main

tiktoken is a fast [BPE](https://en.wikipedia.org/wiki/Byte_pair_encoding) tokeniser for use with OpenAI's models.

The tokeniser API is documented in `tiktoken/core.py`.

Example code using tiktoken can be found in the [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb).

### Performance
1. tiktoken is between 3-6x faster than a comparable open source tokeniser
2. Performance measured on 1GB of text using the GPT-2 tokeniser, using GPT2TokenizerFast from `tokenizers==0.13.2`, `transformers==4.24.0` and `tiktoken==0.2.0`.
