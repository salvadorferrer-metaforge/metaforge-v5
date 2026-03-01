# ============================================================================
# AUTHOR_IDENTITY_BLOCK [ROOT_ACCESS_ONLY]
# ============================================================================
# IDENTIFIER:  Salvador Ferrer
# PROJECT:     METAFORGE_v5 (Community Tools Registry)
# BOOK_REF:    "CÓMO CONSTRUIR AGENTES DE IA QUE NO ALUCINAN"
# STATUS:      COMMUNITY_GATEWAY_ACTIVE
# ============================================================================
# METAFORGE v5 🏗️
> **"La estructura vence a la estocástica. La precisión vence a la ambigüedad."**

[![Libro](https://img.shields.io/badge/Libro-CÓMO_CONSTRUIR_AGENTES_DE_IA_QUE_NO_ALUCINAN-blueviolet.svg)](#)
[![Version](https://img.shields.io/badge/Version-5.0.0--industrial-green.svg)](CHANGELOG.md)
[![License: Dual](https://img.shields.io/badge/License-Dual%20Personal%2FCommercial-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-5.0.0--industrial-green.svg)](CHANGELOG.md)
[![ASI](https://img.shields.io/badge/Paradigma-ASI%20(Artificial%20Specific%20Intelligence)-orange.svg)](docs/que-es-asi.md)

---

## 📖 Descripción

**META FORGE v5** es un **Meta-Agente Constructor Industrial** diseñado para crear **Sistemas de Sabiduría Artificial Específica (ASI)** — agentes deterministas, precisos y predictibles para entornos empresariales críticos.

Este repositorio es el entorno de ejecución oficial y el Atlas de Activos del libro: 
**"CÓMO CONSTRUIR AGENTES DE IA QUE NO ALUCINAN - Manual de producción para ingenieros"** por Salvador Ferrer Moncho.

### 🧩 Componentes del Core

| Activo | Función | Ruta |
| :--- | :--- | :--- |
| **Kernel v5** | System Prompt del Meta-Agente Constructor Industrial. | `core/SYSTEM_PROMPT_MetaForge_v5.md` |
| **Navigator** | Interfaz de control y guía de procedimiento (Bridge). | `core/NAVIGATOR_INTERFACE.md` |
| **Primitives** | Catálogo de 54 primitivas cognitivas validadas. | `core/cognitive_primitives_atlas.json` |
| **Knowledge Anchors** | Libros Maestros (Técnico y Pedagógico) para inyección de contexto. | `core/libro_maestro_conocimiento_*.yml` |

---

## 🚀 Inicio Rápido

### Requisitos Previos

- Acceso a un LLM con capacidad de procesamiento estructurado (GPT-4o, Claude 3.5, Gemini 1.5 Pro)
- Conocimientos básicos de JSON/YAML (para usuarios avanzados)
- El libro "Manual de Ingeniería de Prompt" (recomendado)

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/salvadorferrer/metaforge-v5.git
cd metaforge-v5

# Verificar archivos requeridos
ls -la *.yml *.json *.md
```


### 🚀 Protocolo de Operación (Flujo de Trabajo Industrial)

Para garantizar un **Determinismo del 99.9%**, no intente gestionar el proceso manualmente. Siga estrictamente esta secuencia de inicialización:

1. **Carga del Kernel:** Copie el contenido de `core/SYSTEM_PROMPT_MetaForge_v5.md` y péguelo en el **System Prompt** de su LLM (Recomendado: GLM-5, KIMI, Claude 3.5 Sonnet o GPT-4o).
2. **Activación del Navigator:** Abra una **segunda ventana de chat** con el mismo modelo y pegue el contenido de `core/NAVIGATOR_INTERFACE.md`.
3. **Ejecución Guiada:** A partir de este momento, **interactúe exclusivamente con el Navigator**. Él le indicará paso a paso:
* Cuándo enviar el comando de inicialización al Kernel.
* Qué archivos específicos de la carpeta `core/` debe adjuntar en cada fase.
* Cómo validar los outputs mediante la traza de pensamiento (`<thought_trace>`).



> **REGLA DE ORO:** El Navigator es su torre de control; el Kernel es el motor. No alimente el motor sin las instrucciones de la torre.

---

### 📁 Mapa de Activos del Core

| Activo | Función |
| --- | --- |
| `core/SYSTEM_PROMPT_MetaForge_v5.md` | **Kernel:** El motor de compilación de agentes. |
| `core/NAVIGATOR_INTERFACE.md` | **Navigator:** Su interfaz de guía y control de flujo. |
| `core/cognitive_primitives_atlas.json` | **Biblioteca:** Primitivas para el razonamiento del agente. |
| `core/libro_maestro_*.yml` | **Anclas:** Conocimiento técnico y pedagógico verificado. |

---



## 📁 Estructura del Repositorio

```
metaforge-v5/
├── 📄 LICENSE                    # Licencia dual (Personal/Comercial)
├── 📄 LICENSE-COMMERCIAL         # Términos de licencia enterprise
├── 📄 README.md                  # Este archivo
├── 📄 CHANGELOG.md               # Historial de versiones
├── 📄 CODE_OF_CONDUCT.md         # Código de conducta
├── 📄 CONTRIBUTING.md            # Guía de contribución
├── 📄 SECURITY.md                # Política de seguridad
│
├── 🧠 core/                      # Activos principales
│   ├── SYSTEM_PROMPT_CORE_v5.md  # Meta-agente constructor
│   ├── cognitive_primitives_atlas.json  # 54 primitivas cognitivas
│   ├── libro_maestro_conocimiento_pedagogico.yml
│   └── libro_maestro_conocimiento_tecnico.yml
│
├── 🔧 tools/                     # Herramientas auxiliares
│   ├── NAVIGATOR_INTERFACE.md    # Navigator humano-máquina
│   └── runtime_auditor.md        # Auditor de capacidades
│
├── 📚 docs/                      # Documentación
│   ├── guia_uso.md               # Guía completa de uso
│   ├── que-es-asi.md             # Concepto de ASI
│   ├── arquitectura_doble_modelo.md
│   ├── protocolo_zero_trust.md
│   └── ejemplos/                 # Casos de estudio
│
├── 🎨 community/                 # Contribuciones de la comunidad
│   ├── agents/                   # Agentes creados por usuarios
│   ├── tools/                    # Herramientas adicionales
│   └── integrations/             # Integraciones con sistemas
│
├── 💻 scripts/                   # Scripts de utilidad
│   └── check_license_eligibility.py  # Verificador de licencia
│
└── 📖 libro/                     # Recursos para el libro
    └── insercion_enlace.txt      # Texto para insertar en el libro
```

---

## 🎯 Casos de Uso

### ✅ Uso Gratuito Permitido

- **Aprendizaje personal** del paradigma ASI
- **Investigación académica** sin fines de lucro
- **Proyectos personales** y experimentación
- **Pequeñas empresas** (<250 empleados, <50M€ facturación)
- **Startups en fase inicial** que cumplan umbrales PYME

### 💼 Requiere Licencia Comercial

- **Grandes empresas** (supera umbrales PYME)
- **Integración en productos SaaS**
- **Consultoría de ingeniería de prompts** remunerada
- **Despliegue en sistemas empresariales críticos**
- **Uso en producción** por organizaciones grandes

---

## 📋 Modelo de Licenciamiento Dual

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         MODELO DE LICENCIA DUAL                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  🟢 LICENCIA PERSONAL/PYME (GRATUITA)                                   │
│     ├── Uso personal y educativo                                        │
│     ├── Pequeñas empresas (<250 emp, <50M€)                            │
│     ├── Modificación para uso propio                                    │
│     └── Sin coste                                                       │
│                                                                         │
│  🔵 LICENCIA COMERCIAL ENTERPRISE (DE PAGO)                             │
│     ├── Grandes empresas                                                │
│     ├── Período de prueba: 90 días                                      │
│     ├── Integración en productos SaaS                                   │
│     └── Consultoría remunerada                                          │
│                                                                         │
│  ⚠️  AMBAS LICENCIAS INCLUYEN:                                          │
│     ├── Sin garantías de ningún tipo                                    │
│     ├── Exención de responsabilidad por alucinaciones                   │
│     └── Obligación de supervisión humana                                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Definición de "Gran Empresa"

Según la definición de PYME de la Unión Europea:

| Criterio | Umbral PYME | Gran Empresa |
|----------|-------------|--------------|
| Empleados | < 250 | ≥ 250 |
| Facturación anual | ≤ 50M€ | > 50M€ |
| Balance total | ≤ 43M€ | > 43M€ |

**Sistema de Honor con Auditoría:** El usuario declara su clasificación. El autor se reserva el derecho de solicitar documentación justificativa.

---

## 🔗 Recursos Adicionales

### 📖 Documentación del Libro
- **Título:** CÓMO CONSTRUIR AGENTES DE IA QUE NO ALUCINAN - Manual de producción para ingenieros
- **Autor:** Salvador Ferrer Moncho
- **Disponible en:** Amazon KDP (Kindle y Tapa Blanda)
- **QR al repositorio:** [Ver código QR](#)


---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para:

- Cómo reportar bugs
- Cómo proponer mejoras
- Cómo subir tus agentes a la comunidad
- Estándares de código y documentación

### Áreas de Contribución

- 🧠 Nuevas primitivas cognitivas
- 🔧 Herramientas y utilidades
- 📚 Documentación y tutoriales
- 🌍 Traducciones
- 🐛 Reportes de bugs

---

## 🔒 Seguridad

Para reportar vulnerabilidades de seguridad:

1. **NO** abras un issue público
2. Envía un email a: security@metaforge.ai
3. Incluye pasos de reproducción y impacto
4. Espera 90 días antes de divulgación pública (responsible disclosure)

Consulta [SECURITY.md](SECURITY.md) para más detalles.

---

## ⚠️ Aviso Legal

> **IMPORTANTE:** Los sistemas de IA son estocásticos por naturaleza. Este software se proporciona "TAL CUAL" sin garantías. El autor no se hace responsable de:
> - Alucinaciones o información incorrecta generada
> - Decisiones tomadas basándose en los outputs
> - Daños directos o indirectos derivados del uso
>
> **La supervisión humana es obligatoria para decisiones críticas.**

Consulta [LICENSE](LICENSE) para el texto completo de exención de responsabilidad.

---

## 📊 Estadísticas del Proyecto

| Métrica | Valor |
|---------|-------|
| Primitivas Cognitivas | 54 |
| Fases del Pipeline | 5 |
| Sectores Soportados | 8+ |
| Idiomas | Español, Inglés |
| Licencia | Dual (Personal/Comercial) |

---

## 🙏 Agradecimientos

- A la comunidad de ingeniería de prompts por el feedback continuo
- A los colaboradores que han contribuido primitivas y herramientas
- A los lectores del libro que hacen posible este proyecto

---

## 📜 Cita Este Proyecto

```bibtex
@book{ferrer2026alucinaciones,
  title={CÓMO CONSTRUIR AGENTES DE IA QUE NO ALUCINAN: Manual de producción para ingenieros},
  author={Ferrer Moncho, Salvador},
  year={2026},
  publisher={Publicación Independiente / Amazon KDP},
  url={https://github.com/[TU_USUARIO]/metaforge-v5}
}
```

---

<div align="center">

**[⬆ Volver al inicio](#meta-forge-v5-)**

*Copyright © 2026 Salvador Ferrer Moncho*

*"Dejar de escribir prompts. Empezar a diseñar arquitecturas."*

</div>
