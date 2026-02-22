# Guía de Contribución a META FORGE v5

> "La comunidad que construye juntos, aprende juntos."

Gracias por tu interés en contribuir al proyecto META FORGE v5. Esta guía te ayudará a participar de manera efectiva.

---

## 📋 Índice

- [Código de Conducta](#código-de-conducta)
- [Cómo Contribuir](#cómo-contribuir)
- [Áreas de Contribución](#áreas-de-contribución)
- [Proceso de Envío](#proceso-de-envío)
- [Estructura de la Comunidad](#estructura-de-la-comunidad)
- [Preguntas Frecuentes](#preguntas-frecuentes)

---

## 🤝 Código de Conducta

Este proyecto sigue nuestro [Código de Conducta](CODE_OF_CONDUCT.md). Al participar, te comprometes a:

- Ser respetuoso con todos los miembros
- Aceptar críticas constructivas
- Priorizar el bienestar de la comunidad
- Mostrar empatía hacia otros

---

## 🚀 Cómo Contribuir

### 1. Reportar Bugs

Si encuentras un error:

1. **Verifica** que no haya sido reportado antes (busca en Issues)
2. **Abre un nuevo Issue** usando la plantilla de bug
3. **Incluye**:
   - Descripción clara del problema
   - Pasos para reproducir
   - Comportamiento esperado vs actual
   - Entorno (modelo LLM, versión, etc.)
   - Screenshots o logs si aplica

### 2. Proponer Mejoras

Para sugerir nuevas características:

1. **Abre un Issue** con etiqueta `enhancement`
2. **Describe** el problema que resuelve
3. **Explica** cómo encaja con la filosofía ASI
4. **Proporciona** ejemplos de uso si es posible

### 3. Contribuir Código/Agentes

Para enviar tus creaciones a la comunidad:

```bash
# 1. Fork el repositorio
git clone https://github.com/TU_USUARIO/metaforge-v5.git

# 2. Crea una rama para tu contribución
git checkout -b feature/nueva-primitiva-o-agente

# 3. Coloca tus archivos en la carpeta community/
#    - Agentes: community/agents/tu-agente/
#    - Herramientas: community/tools/tu-herramienta/

# 4. Sigue las plantillas proporcionadas

# 5. Commit y push
git add .
git commit -m "Add: [tipo] Descripción clara"
git push origin feature/nueva-primitiva-o-agente

# 6. Abre un Pull Request
```

---

## 🎯 Áreas de Contribución

### 🧠 Nuevas Primitivas Cognitivas

**Ubicación:** `community/primitives/`

**Formato:** Archivo JSON siguiendo el schema del atlas

**Requisitos:**
- Identificador único (ej: `COGPROC_055`)
- Descripción del efecto cognitivo
- Triggers (principal + variantes)
- Métricas de validación
- Casos de uso documentados

**Ejemplo mínimo:**
```json
{
  "primitive_id": "COGPROC_055",
  "name": "Mi Nueva Primitiva",
  "category": "cognitive_processes",
  "trigger": {
    "primary": "Texto del trigger",
    "variants": ["Variante 1", "Variante 2"]
  },
  "effect": "Descripción del efecto cognitivo",
  "confidence_score": 0.85,
  "submitted_by": "@tu_usuario"
}
```

### 🤖 Agentes de la Comunidad

**Ubicación:** `community/agents/nombre-del-agente/`

**Archivos requeridos:**
- `README.md` (usar plantilla proporcionada)
- `system_prompt.xml` o `system_prompt.yaml`
- `ejemplos/` (casos de uso)
- `LICENSE` (debe ser compatible con licencia dual)

**Plantilla:** Ver `community/agents/PLANTILLA_README.md`

### 🔧 Herramientas y Utilidades

**Ubicación:** `community/tools/nombre-de-la-herramienta/`

**Tipos aceptados:**
- Scripts de automatización
- Validadores de sintaxis
- Convertidores de formato
- Dashboards de monitoreo
- Integraciones con APIs

### 📚 Documentación

**Ubicación:** `docs/`

**Contenidos bienvenidos:**
- Tutoriales paso a paso
- Guías de mejores prácticas
- Traducciones
- Casos de estudio detallados

---

## 📁 Estructura de la Comunidad

```
community/
├── agents/
│   ├── PLANTILLA_README.md          # Plantilla obligatoria
│   ├── README.md                    # Índice de agentes
│   └── [tu-agente]/
│       ├── README.md                # Documentación del agente
│       ├── system_prompt.xml        # Prompt del sistema
│       ├── ejemplos/                # Casos de uso
│       └── LICENSE                  # Licencia del agente
│
├── tools/
│   ├── README.md                    # Índice de herramientas
│   └── [tu-herramienta]/
│       ├── README.md
│       ├── codigo/
│       └── ejemplos/
│
├── integrations/
│   ├── README.md                    # Índice de integraciones
│   └── [sistema]/
│       ├── README.md
│       └── archivos-de-integracion
│
└── primitives/
    ├── README.md                    # Guía de contribución
    └── propuestas/                  # Primitivas en revisión
```

---

## ✅ Proceso de Revisión

### Para Contribuciones a la Comunidad

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Envío     │ -> │  Revisión   │ -> │  Feedback   │ -> │  Aprobación │
│    (PR)     │    │  (7 días)   │    │  (si aplica)│    │  (Merge)    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

**Criterios de revisión:**
- ✅ Cumple con la plantilla proporcionada
- ✅ Incluye documentación adecuada
- ✅ No viola derechos de terceros
- ✅ Licencia compatible
- ✅ Funcionalidad verificable

### Para Cambios al Código Fuente

Los archivos en `core/` y `tools/` son de **solo lectura** para la comunidad.

Solo el autor y colaboradores designados pueden modificar:
- `SYSTEM_PROMPT_CORE_v5.md`
- `cognitive_primitives_atlas.json`
- `libro_maestro_conocimiento_*.yml`

---

## 📝 Estándares de Documentación

### Para Agentes

```markdown
# Nombre del Agente

## Descripción
Breve descripción de qué hace el agente.

## Dominio
Área de especialización (Legal, HR, Fintech, etc.)

## Requisitos
- Modelo LLM recomendado
- Herramientas necesarias
- Contexto mínimo requerido

## Uso
Instrucciones de cómo usar el agente.

## Ejemplos
Casos de uso con inputs y outputs.

## Limitaciones
Qué NO puede hacer el agente.

## Licencia
Debe especificar licencia compatible.

## Autor
@tu_usuario | tu@email.com
```

### Para Commits

Formato: `[tipo]: descripción corta`

Tipos:
- `Add:` Nueva característica
- `Fix:` Corrección de bug
- `Docs:` Cambios en documentación
- `Refactor:` Reestructuración de código
- `Test:` Adición de tests

---

## ❓ Preguntas Frecuentes

### ¿Puedo vender un agente que creé usando META FORGE?

**Sí**, pero con condiciones:
- Si eres PYME: Puedes ofrecer servicios basados en tus agentes
- Si eres Gran Empresa: Necesitas licencia comercial
- Debes respetar la licencia dual del sistema base

### ¿Puedo modificar los archivos fuente?

**No.** Los archivos en `core/` son de solo lectura. Puedes:
- Crear forks personales
- Proponer mejoras mediante Issues
- Contribuir a la carpeta `community/`

### ¿Cuánto tarda en revisarse mi contribución?

- **Agentes/Herramientas:** 7 días hábiles
- **Primitivas:** 14 días (requiere validación más rigurosa)
- **Documentación:** 3-5 días hábiles

### ¿Qué pasa si mi contribución es rechazada?

Recibirás feedback detallado. Puedes:
- Corregir y reenviar
- Mantener en tu fork personal
- Discutir en el Issue abierto

---

## 📞 Contacto

- **Soporte general:** support@metaforge.ai
- **Contribuciones:** contributing@metaforge.ai
- **Discord:** [Unirse al servidor](https://discord.gg/metaforge)

---

## 🌟 Reconocimientos

Los contribuyentes destacados serán reconocidos en:
- El archivo `CONTRIBUTORS.md`
- La sección de agradecimientos del libro
- Eventos de la comunidad

---

<div align="center">

**¡Gracias por contribuir al futuro de la Ingeniería de Software Cognitivo!**

</div>
