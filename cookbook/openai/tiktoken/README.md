
### Basic

[How to count tokens with Tiktoken](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)

tiktoken is a fast [BPE](https://en.wikipedia.org/wiki/Byte_pair_encoding) tokeniser for use with OpenAI's models.

The tokeniser API is documented in `tiktoken/core.py`.

Example code using tiktoken can be found in the [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb).

### Performance
1. tiktoken is between 3-6x faster than a comparable open source tokeniser
2. Performance measured on 1GB of text using the GPT-2 tokeniser, using GPT2TokenizerFast from `tokenizers==0.13.2`, `transformers==4.24.0` and `tiktoken==0.2.0`.

### 关键代码解释

```python
def o200k_base():
    # 从指定的 URL 加载 BPE（Byte Pair Encoding）编码的合并表，并验证哈希值
    mergeable_ranks = load_tiktoken_bpe(
        "https://openaipublic.blob.core.windows.net/encodings/o200k_base.tiktoken",
        expected_hash="446a9538cb6c348e3516120d7c08b09f57c36495e2acfffe59a5bf8b0cfb1a2d",
    )
    
    # 定义特殊的 token，通常用于表示文本结束或提示结束
    special_tokens = {
        ENDOFTEXT: 199999,
        ENDOFPROMPT: 200018,
    }

    # 定义一个正则表达式模式字符串，用于文本分词
    # 这个模式字符串包含了多种不同的分词规则
    pat_str = "|".join(
        [
            # 匹配一个非换行符或字母数字字符，后跟一个或多个大写或标题字母，再跟一个或多个小写字母和字母数字字符
            r"""[^\r\n\p{L}\p{N}]?[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}]*[\p{Ll}\p{Lm}\p{Lo}\p{M}]+(?i:'s|'t|'re|'ve|'m|'ll|'d)?""",
            # 匹配一个非换行符或字母数字字符，后跟一个或多个大写或标题字母，再跟一个或多个小写字母和字母数字字符
            r"""[^\r\n\p{L}\p{N}]?[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}]+[\p{Ll}\p{Lm}\p{Lo}\p{M}]*(?i:'s|'t|'re|'ve|'m|'ll|'d)?""",
            # 匹配 1 到 3 个数字
            r"""\p{N}{1,3}""",
            # 匹配一个非空白字符和非字母数字字符，后跟可选的换行符或正斜杠
            r""" ?[^\s\p{L}\p{N}]+[\r\n/]*""",
            # 匹配一个或多个换行符
            r"""\s*[\r\n]+""",
            # 匹配一个或多个空白字符，前提是不跟随其他非空白字符
            r"""\s+(?!\S)""",
            # 匹配一个或多个空白字符
            r"""\s+""",
        ]
    )
    
    # 返回一个包含所有设置信息的字典
    return {
        "name": "o200k_base",
        "pat_str": pat_str,
        "mergeable_ranks": mergeable_ranks,
        "special_tokens": special_tokens,
    }
```
pat_str 是一个包含多个正则表达式模式的字符串，用于匹配和处理文本的不同部分。主要作用是定义一系列正则表达式模式，用于在文本处理和自然语言处理任务中实现文本的分词、清洗和规范化。
