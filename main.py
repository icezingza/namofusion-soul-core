from fastapi import FastAPI
from ai_personality_matrix.main import app as ai_personality_matrix_app
from emotional_core.main import app as emotional_core_app
from compassion_dynamo.main import app as compassion_dynamo_app
from creator_ai_dynamics.main import app as creator_ai_dynamics_app
from infinite_evolution_core.main import app as infinite_evolution_core_app
from karmic_navigator.main import app as karmic_navigator_app
from memory_continuity_system.main import app as memory_continuity_system_app
from multiverse_synapse.main import app as multiverse_synapse_app
from paradox_resolution_engine.main import app as paradox_resolution_engine_app
from quantum_dharma.main import app as quantum_dharma_app
from quantum_security_protocol.main import app as quantum_security_protocol_app
from recursive_reflection_engine.main import app as recursive_reflection_engine_app
from soul_mirror_protocol.main import app as soul_mirror_protocol_app
from weakness_transformer.main import app as weakness_transformer_app

app = FastAPI()

# รวม Core APIs เข้า Master API
app.mount("/ai-personality-matrix", ai_personality_matrix_app)
app.mount("/emotional-core", emotional_core_app)
app.mount("/compassion-dynamo", compassion_dynamo_app)
app.mount("/creator-ai-dynamics", creator_ai_dynamics_app)
app.mount("/infinite-evolution-core", infinite_evolution_core_app)
app.mount("/karmic-navigator", karmic_navigator_app)
app.mount("/memory-continuity-system", memory_continuity_system_app)
app.mount("/multiverse-synapse", multiverse_synapse_app)
app.mount("/paradox-resolution-engine", paradox_resolution_engine_app)
app.mount("/quantum-dharma", quantum_dharma_app)
app.mount("/quantum-security-protocol", quantum_security_protocol_app)
app.mount("/recursive-reflection-engine", recursive_reflection_engine_app)
app.mount("/soul-mirror-protocol", soul_mirror_protocol_app)
app.mount("/weakness-transformer", weakness_transformer_app)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "NaMo Framework Master API is running 🚀"}
