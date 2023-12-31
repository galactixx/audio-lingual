from enum import Enum

class OpenAIInstructions(Enum):
    """
    System instruction options for OpenAI.
    """
    BASIC = {"role": "system", "content": "you are a helpful friend"}

class OpenAIModels(Enum):
    """
    All OpenAI models available through API.
    """
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_0301 = "gpt-3.5-turbo-0301"
    GPT_3_5_TURBO_0613 = "gpt-3.5-turbo-0613"

    GPT_4 = "gpt-4"
    GPT_4_0314 = "gpt-4-0314"
    GPT_4_0613 = "gpt-4-0613"

class TTSModels(Enum):
    """
    TTS model options for Coqui and ElevenLabs.
    """
    ELEVEN_LABS_ENGLISH_V1 = 'eleven_english_v1'
    ELEVEN_LABS_MULTILINGUAL_V1 = "eleven_multilingual_v1"
    ELEVEN_LABS_MULTILINGUAL_V2 = "eleven_multilingual_v2"

    COQUI_GLOW_TTS = 'glow-tts'

class CoquiModelGroup(Enum):
    """
    Coqui model groups.
    """
    LJSPEECH = 'ljspeech'
