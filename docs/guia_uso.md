# ============================================================================
# AUTHOR_IDENTITY_BLOCK [ROOT_ACCESS_ONLY]
# ============================================================================
# IDENTIFIER:  Salvador Ferrer
# PROJECT:     METAFORGE_v5 (Community Tools Registry)
# BOOK_REF:    "CÓMO CONSTRUIR AGENTES DE IA QUE NO ALUCINAN"
# STATUS:      COMMUNITY_GATEWAY_ACTIVE
# ============================================================================

# Guía de Uso de SYSTEM_PROMPT_MetaForge_v5.md

> Manual completo para construir agentes ASI con SYSTEM_PROMPT_MetaForge_v5.md.

---

## 📖 Índice
## ⚡ Protocolo de Arranque (Quick Start)

Para inicializar el kernel de **SYSTEM_PROMPT_MetaForge_v5.md** con la fidelidad mostrada en los logs de la sesión `META_SESSION_20260130_07347_AF42`, ejecute esta secuencia:

1. **Carga del Kernel:** Pegue el contenido de `core/SYSTEM_PROMPT_MetaForge_v5.md` en el System Prompt.
2. **Inyección de Primitivas:** Proporcione el archivo `core/cognitive_primitives_atlas.json` y los Libros Maestros (`libro_maestro_*.yml`) cuando el Navigator lo solicite.
3. **Comando de Ignición:** > "Arquitecto, inicialice modo COMPILACIÓN INDUSTRIAL. Verifique integridad de Primitivas y establezca el AirGap operativo."
---
1. [Conceptos Fundamentales](#conceptos-fundamentales)
2. [Preparación](#preparación)
3. [Pipeline de Construcción](#pipeline-de-construcción)
4. [Casos de Uso](#casos-de-uso)
5. [Solución de Problemas](#solución-de-problemas)

---

## Conceptos Fundamentales

### ¿Qué es ASI?

**Artificial Specific Intelligence (ASI)** es un sistema diseñado arquitectónicamente para:

1. Poseer conocimiento profundo en un **dominio extremadamente acotado**
2. Conocer con precisión los **límites de su ignorancia**
3. Estar **prohibido de alucinar** fuera de esos límites

> **Diferencia clave:** La ASI no busca ser generalista como la AGI, sino experto determinista en un ámbito específico.

### El Paradigma de Compilación

```
CONVERSACIÓN (Antiguo)          COMPILACIÓN (Nuevo)
─────────────────────           ───────────────────
"Hola, ¿puedes..."      →       YAML/JSON estructurado
Lenguaje natural        →       Bytecode cognitivo
Ambiguo                 →       Determinista
Iterativo               →       One-shot preciso
```

### Arquitectura de Doble Modelo

```
┌─────────────────┐         ┌─────────────────┐
│   NODO 1        │         │   NODO 2        │
│   CÓMPLICE      │───────→│   ENSAMBLADOR   │
│                 │         │                 │
│ • Conversa      │  AirGap │ • Entorno       │
│ • Diseña        │────────→│   estéril       │
│ • Especifica    │         │ • Ejecuta       │
│                 │         │ • Construye     │
└─────────────────┘         └─────────────────┘
   Diseño Caótico              Ejecución Pura
```

---

## Preparación

### Requisitos

1. **LLM Compatible**
   - GLM-5
   - KIMI
   - GPT-4o (OpenAI)
   - Claude 3.5 Sonnet (Anthropic)
   - Gemini 1.5 Pro (Google)
   - Llama 3.1 70B (Local)

2. **Archivos Base**
   - `libro_maestro_conocimiento_pedagogico.yml`
   - `libro_maestro_conocimiento_tecnico.yml`
   - `cognitive_primitives_atlas.json`

3. **Conocimientos Previos**
   - JSON/YAML básico
   - Conceptos de prompting
   - Dominio de aplicación objetivo

### Configuración Inicial

```bash
# 1. Clonar repositorio
git clone https://github.com/salvadorferrer/metaforge-v5.git

# 2. Verificar archivos
ls -la *.yml *.json

# 3. Cargar en tu LLM favorito
# (Subir los 3 archivos a la ventana de contexto)
```

---

## Pipeline de Construcción

### Fase 0: Perfilado y Contexto

**Objetivo:** Entender al usuario y el dominio

**Input:**
```yaml
INICIALIZAR_METAFORGE_v5
[MODE]: OPERATOR_DRIVEN
[PROFILE]: PER_02_EXPERTO
```

**Output:**
- Perfil de usuario detectado
- Modo de operación establecido

---

### Fase 1: Análisis de Dominio

**Objetivo:** Extraer anclas de conocimiento del sector

**Pasos:**

1. **Especificar dominio**
   ```
   Dominio: [Legal/HR/Fintech/Healthcare/etc.]
   ```

2. **Extraer anclas** (3 opciones):
   - **Opción 1:** Usar búsqueda web del modelo
   - **Opción 2:** Prompt externo (Perplexity/Claude con web)
   - **Opción 3:** Pegar JSON de anclas ya verificado

3. **Validar anclas**
   - Verificar fuentes
   - Comprobar vigencia
   - Asignar scores de confianza

**Output:**
```json
{
  "business_anchors_industrial": {
    "domain": "Legal",
    "anchors": {
      "regulatory": [...],
      "technical_standards": [...],
      "business_metrics": [...]
    }
  }
}
```

---

### Fase 2: Auditoría de Runtime

**Objetivo:** Caracterizar el LLM objetivo

**Preguntas clave:**
- ¿Qué modelo usarás para el agente final?
- ¿Tiene acceso a web?
- ¿Tiene Python sandbox?
- ¿Cuál es su fecha de corte?

**Prompt de auditoría:**
```yaml
# AUDITORÍA DE RUNTIME v5
Modelo: {{MODEL_NAME}}
Entorno: {{DEPLOYMENT_ENV}}

EJECUTAR:
1. Characterizar capacidades básicas
2. Identificar especializaciones
3. Documentar limitaciones
4. Mapear comportamientos no deterministas
```

**Output:**
```json
{
  "runtime_characteristics": {
    "model_name": "GPT-4o",
    "context_window_tokens": 128000,
    "knowledge_cutoff_date": "2023-10",
    "json_reliability_score": 0.94
  }
}
```

---

### Fase 3: Diseño Cognitivo

**Objetivo:** Seleccionar y configurar primitivas

**Proceso:**

1. **Cargar resultados** de Fases 1 y 2
2. **Aplicar matriz** de selección Dominio × Modelo × Perfil
3. **Calcular scores** de adecuación (0-100)
4. **Seleccionar** Top 15-25 primitivas
5. **Diseñar** patrones compuestos

**Matriz de selección:**
```
Score = (domain_relevance × 0.4) + 
        (model_compatibility × 0.3) + 
        (compliance_support × 0.3)
```

**Output:**
```json
{
  "cognitive_design": {
    "selected_primitives": [...],
    "composite_patterns": [...],
    "confidence_calculation": "..."
  }
}
```

---

### Fase 4: Ensamblaje Industrial

**Objetivo:** Generar el system prompt final

**Componentes:**

1. **Identity Module**
   ```yaml
   IDENTITY:
     Role: "Senior [Dominio] Specialist"
     Domain_Lock: ["...", "..."]
   ```

2. **Business Anchors Integration**
   ```yaml
   KNOWLEDGE_ANCHORS:
     - "[Ancla 1]"
     - "[Ancla 2]"
   ```

3. **Cognitive Primitives Engine**
   ```yaml
   THOUGHT_PROCESS:
     - "[COGPROC_XXX]"
     - "[THSTR_XXX]"
   ```

4. **Guardrails**
   ```yaml
   GUARDRAILS:
     - "NEVER ..."
     - "ALWAYS ..."
   ```

**Output:**
```xml
<SYSTEM_KERNEL>
  <IDENTITY>...</IDENTITY>
  <KNOWLEDGE>...</KNOWLEDGE>
  <OPERATIONAL_PROTOCOL>...</OPERATIONAL_PROTOCOL>
  <GUARDRAILS>...</GUARDRAILS>
  <OUTPUT_INTERFACE>...</OUTPUT_INTERFACE>
</SYSTEM_KERNEL>
```

---

### Fase 5: Paquete de Despliegue

**Objetivo:** Empaquetar todo para producción

**Modos disponibles:**

| Modo | Archivos | Tiempo | Uso |
|------|----------|--------|-----|
| Express | 3 | 5-10 min | Demos, prototipos |
| Standard | 7 | 20-30 min | Producción básica |
| Enterprise | 14+ | 45-90 min | Misión crítica |

**Contenido Enterprise:**
- Agent XML completo
- Business anchors JSON
- Runtime audit JSON
- Cognitive design JSON
- Validation suite Python
- Terraform/K8s manifests
- Dashboard de monitoreo
- Runbook de incidentes

---

## Casos de Uso

### Caso 1: Agente Legal (THEMIS)

**Dominio:** Derecho administrativo español

**Anclas principales:**
- Art. 40.2 LPACAP (notificaciones)
- Art. 112 LSV (prescripción)
- Non bis in idem

**Primitivas aplicadas:**
- COGPROC_003 (Dialectical Synthesis)
- PROFSPEC_006 (Legal Reasoning)
- AUTOREG_002 (Confidence Calibration)

**Resultado:**
Agente que identifica vicios de forma para anular procedimientos.

---

### Caso 2: Agente de Verificación (ARVA)

**Dominio:** Validación factual

**Características:**
- Fuentes solo hasta fecha de corte
- Atribución forzada [Institución](Año)
- Silencio preferible a error

**Resultado:**
Agente filtro epistémico con máxima precisión factual.

---

## Solución de Problemas

### Problema: El agente ignora formato JSON

**Causas posibles:**
- System prompt no especifica formato estrictamente
- Falta ejemplo de salida
- Temperatura demasiado alta

**Soluciones:**
```yaml
# Nivel 1: Guardrails explícitos
GUARDRAILS:
  - "RESPOND ONLY IN JSON. NO TEXT."

# Nivel 2: Ejemplo completo
OUTPUT_INTERFACE:
  example: '{"status": "success", "data": {}}'

# Nivel 3: Temperatura baja
parameters:
  temperature: 0.1
```

### Problema: Alucinaciones en datos legales

**Causa:** Dependencia de memoria interna obsoleta

**Solución:**
```yaml
KNOWLEDGE_PROTOCOL:
  TRUST_HIERARCHY:
    LEGAL_MEMORY: "LOW_TRUST"
  VERIFICATION_TRIGGER:
    SCOPE: ["Legal_Compliance"]
    ACTION: "FORCE_EXECUTION(tool:legal_search)"
```

### Problema: El agente se desvía de su rol

**Causa:** RLHF induce comportamiento servicial

**Solución:**
```yaml
IDENTITY:
  Domain_Lock: ["Dominio específico"]
  
GUARDRAILS:
  - "NEVER provide moral guidance"
  - "tone: 'Clinical, Ruthless, Zero-Sugar'"
```

---

## 📚 Recursos Adicionales

- [CÓMO CONSTRUIR AGENTES DE IA QUE NO ALUCINAN](https://github.com/salvadorferrer/metaforge-v5)
- [Cognitive Primitives Atlas](../cognitive_primitives_atlas.json)
- [Libro Maestro Técnico](../libro_maestro_conocimiento_tecnico.yml)

---

<div align="center">

**[⬆ Volver al inicio](#guía-de-uso-de-meta-forge-v5)**

*¿Preguntas? Abre un [Issue](https://github.com/salvadorferrer/metaforge-v5/issues)*

</div>
