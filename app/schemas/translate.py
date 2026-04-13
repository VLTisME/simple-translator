from enum import Enum
from pydantic import BaseModel, Field, ConfigDict, field_validator

LANGUAGE_ALIASES = {
    "afrikaans": "af_ZA",
    "arabic": "ar_AR",
    "azerbaijani": "az_AZ",
    "bengali": "bn_IN",
    "czech": "cs_CZ",
    "german": "de_DE",
    "english": "en_XX",
    "spanish": "es_XX",
    "estonian": "et_EE",
    "persian": "fa_IR",
    "finnish": "fi_FI",
    "french": "fr_XX",
    "galician": "gl_ES",
    "gujarati": "gu_IN",
    "hebrew": "he_IL",
    "hindi": "hi_IN",
    "croatian": "hr_HR",
    "indonesian": "id_ID",
    "italian": "it_IT",
    "japanese": "ja_XX",
    "georgian": "ka_GE",
    "kazakh": "kk_KZ",
    "khmer": "km_KH",
    "korean": "ko_KR",
    "lithuanian": "lt_LT",
    "latvian": "lv_LV",
    "macedonian": "mk_MK",
    "malayalam": "ml_IN",
    "mongolian": "mn_MN",
    "marathi": "mr_IN",
    "burmese": "my_MM",
    "nepali": "ne_NP",
    "dutch": "nl_XX",
    "polish": "pl_PL",
    "pashto": "ps_AF",
    "portuguese": "pt_XX",
    "romanian": "ro_RO",
    "russian": "ru_RU",
    "sinhala": "si_LK",
    "slovene": "sl_SI",
    "swedish": "sv_SE",
    "swahili": "sw_KE",
    "tamil": "ta_IN",
    "telugu": "te_IN",
    "thai": "th_TH",
    "tagalog": "tl_XX",
    "turkish": "tr_TR",
    "ukrainian": "uk_UA",
    "urdu": "ur_PK",
    "vietnamese": "vi_VN",
    "xhosa": "xh_ZA",
    "chinese": "zh_CN"
}

class LanguageEnum(str, Enum):
    """ mbart's supported languages"""
    ARABIC = "ar_AR"
    CZECH = "cs_CZ"
    GERMAN = "de_DE"
    ENGLISH = "en_XX"
    SPANISH = "es_XX"
    ESTONIAN = "et_EE"
    FINNISH = "fi_FI"
    FRENCH = "fr_XX"
    GUJARATI = "gu_IN"
    HINDI = "hi_IN"
    ITALIAN = "it_IT"
    JAPANESE = "ja_XX"
    KAZAKH = "kk_KZ"
    KOREAN = "ko_KR"
    LITHUANIAN = "lt_LT"
    LATVIAN = "lv_LV"
    BURMESE = "my_MM"
    NEPALI = "ne_NP"
    DUTCH = "nl_XX"
    ROMANIAN = "ro_RO"
    RUSSIAN = "ru_RU"
    SINHALA = "si_LK"
    TURKISH = "tr_TR"
    VIETNAMESE = "vi_VN"
    CHINESE = "zh_CN"

    AFRIKAANS = "af_ZA"
    AZERBAIJANI = "az_AZ"
    BENGALI = "bn_IN"
    PERSIAN = "fa_IR"
    HEBREW = "he_IL"
    CROATIAN = "hr_HR"
    INDONESIAN = "id_ID"
    GEORGIAN = "ka_GE"
    KHMER = "km_KH"
    MACEDONIAN = "mk_MK"
    MALAYALAM = "ml_IN"
    MONGOLIAN = "mn_MN"
    MARATHI = "mr_IN"
    POLISH = "pl_PL"
    PASHTO = "ps_AF"
    PORTUGUESE = "pt_XX"
    SWEDISH = "sv_SE"
    SWAHILI = "sw_KE"
    TAMIL = "ta_IN"
    TELUGU = "te_IN"
    THAI = "th_TH"
    TAGALOG = "tl_XX"
    UKRAINIAN = "uk_UA"
    URDU = "ur_PK"
    XHOSA = "xh_ZA"
    GALICIAN = "gl_ES"
    SLOVENE = "sl_SI"

class TranslationParameters(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    src_lang: LanguageEnum = Field(..., description='source language')
    tgt_lang: LanguageEnum = Field(..., description='target language')

    @field_validator("src_lang", "tgt_lang", mode="before")
    @classmethod
    def normalize_language(cls, value):
        if isinstance(value, str):
            value = value.strip().lower()

            # nếu là alias
            if value in LANGUAGE_ALIASES:
                value = LANGUAGE_ALIASES[value]
            elif value not in [e.value for e in LanguageEnum]:
                raise ValueError(f"Unsupported languages: {value}")

        return value    
class TranslationRequest(BaseModel):
    model_config = ConfigDict(extra='forbid')
    inputs: str = Field(...)
    parameters: TranslationParameters = Field(..., description='src_lang, tgt_lang')

class TranslationResponse(BaseModel):
    translation_text: str = Field(...)