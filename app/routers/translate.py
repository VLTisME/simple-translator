from fastapi import APIRouter, HTTPException
from ..schemas.translate import TranslationRequest, TranslationResponse
from ..services.translate import translate

router = APIRouter()

@router.post("/generate", response_model=TranslationResponse)
def translate_text(request: TranslationRequest):
    try:
        result = translate(request.model_dump())
        
        if not isinstance(result, dict) or len(result) == 0:
            raise HTTPException(status_code=502, detail='Invalid response from translation model')
        
        return result

    except:
        raise