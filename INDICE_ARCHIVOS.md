# Índice de Archivos Generados - META FORGE v5

> Documento de referencia con todos los archivos del paquete de implementación.

---

## 📁 Estructura Completa del Repositorio

```
metaforge-v5/
├── 📄 Archivos Raíz
│   ├── LICENSE                              # Licencia dual (Personal/Comercial)
│   ├── LICENSE-COMMERCIAL                   # Términos de licencia enterprise
│   ├── README.md                            # Documentación principal
│   ├── CHANGELOG.md                         # Historial de versiones
│   ├── CODE_OF_CONDUCT.md                   # Código de conducta
│   ├── CONTRIBUTING.md                      # Guía de contribución
│   ├── SECURITY.md                          # Política de seguridad
│   ├── PLAN_DE_ACCION.md                    # Plan completo de implementación
│   └── INDICE_ARCHIVOS.md                   # Este archivo
│
├── 🧠 core/                                 # ACTIVOS PRINCIPALES (Solo Lectura)
│   ├── SYSTEM_PROMPT_CORE_v5_CORREGIDO-v1.md    # Meta-agente constructor
│   ├── cognitive_primitives_atlas.json          # 54 primitivas cognitivas
│   ├── libro_maestro_conocimiento_pedagogico.yml
│   ├── libro_maestro_conocimiento_tecnico.yml
│   └── Operador de Enlace para METAFORGE.md     # Navigator
│
├── 📚 docs/                                 # Documentación
│   ├── guia_uso.md                          # Guía completa de uso
│   ├── github_setup_guide.md                # Configuración de GitHub
│   ├── que-es-asi.md                        # [Por crear] Concepto ASI
│   ├── arquitectura_doble_modelo.md         # [Por crear] Doble Modelo
│   ├── protocolo_zero_trust.md              # [Por crear] Zero-Trust
│   └── ejemplos/                            # Casos de estudio
│       ├── themis.md                        # [Por crear] Agente legal
│       └── arva.md                          # [Por crear] Agente verificación
│
├── 🎨 community/                            # Contribuciones de la Comunidad
│   ├── agents/
│   │   ├── README.md                        # Índice de agentes
│   │   ├── PLANTILLA_README.md              # Plantilla obligatoria
│   │   ├── themis/                          # [Por crear] Agente THEMIS
│   │   └── arva/                            # [Por crear] Agente ARVA
│   ├── tools/
│   │   └── README.md                        # Índice de herramientas
│   ├── integrations/
│   │   └── README.md                        # Índice de integraciones
│   └── primitives/
│       └── README.md                        # [Por crear] Primitivas propuestas
│
├── 💻 scripts/                              # Utilidades
│   └── check_license_eligibility.py         # Verificador de licencia
│
├── 📖 libro/                                # Recursos para el Libro
│   └── insercion_enlace.txt                 # Texto para insertar en el libro
│
├── 🔧 .github/                              # Configuración GitHub
│   ├── workflows/                           # GitHub Actions
│   │   ├── protect-core.yml                 # [Por crear] Protección core/
│   │   └── welcome.yml                      # [Por crear] Bienvenida
│   ├── ISSUE_TEMPLATE/                      # Plantillas de issues
│   │   ├── bug_report.md                    # [Por crear]
│   │   └── feature_request.md               # [Por crear]
│   ├── PULL_REQUEST_TEMPLATE.md             # [Por crear]
│   └── CODEOWNERS                           # [Por crear] Dueños de código
│
└── 🎨 assets/                               # Recursos gráficos
    └── [Por poblar con logos, banners, etc.]
```

---

## 📋 Descripción Detallada de Archivos

### Archivos de Licencia

| Archivo | Propósito | Idioma |
|---------|-----------|--------|
| `LICENSE` | Licencia dual completa con definiciones de PYME | Español/Inglés |
| `LICENSE-COMMERCIAL` | Términos específicos para licencia enterprise | Inglés |

**Cláusulas clave incluidas:**
- ✅ Definición de PYME (<250 emp, <50M€)
- ✅ Período de prueba (90 días)
- ✅ Sistema de honor con auditoría
- ✅ Exención de responsabilidad completa
- ✅ Jurisdicción española

### Archivos de Documentación Principal

| Archivo | Contenido | Audiencia |
|---------|-----------|-----------|
| `README.md` | Inicio rápido, estructura, enlaces | Todos |
| `CHANGELOG.md` | Historial de versiones | Desarrolladores |
| `CONTRIBUTING.md` | Cómo contribuir | Contribuyentes |
| `CODE_OF_CONDUCT.md` | Normas de comportamiento | Comunidad |
| `SECURITY.md` | Reporte de vulnerabilidades | Seguridad |

### Activos Principales (core/)

| Archivo | Tamaño Est. | Descripción |
|---------|-------------|-------------|
| `SYSTEM_PROMPT_CORE_v5_CORREGIDO-v1.md` | ~100KB | Meta-agente constructor con pipeline de 5 fases |
| `cognitive_primitives_atlas.json` | ~200KB | 54 primitivas cognitivas con métricas |
| `libro_maestro_conocimiento_pedagogico.yml` | ~20KB | Base pedagógica con perfiles de aprendizaje |
| `libro_maestro_conocimiento_tecnico.yml` | ~30KB | Base técnica con metodologías y anclas |
| `Operador de Enlace para METAFORGE.md` | ~10KB | Navigator de 8 estados |

### Documentación Técnica (docs/)

| Archivo | Estado | Prioridad |
|---------|--------|-----------|
| `guia_uso.md` | ✅ Completo | Alta |
| `github_setup_guide.md` | ✅ Completo | Alta |
| `que-es-asi.md` | 📝 Pendiente | Media |
| `arquitectura_doble_modelo.md` | 📝 Pendiente | Media |
| `protocolo_zero_trust.md` | 📝 Pendiente | Media |

### Comunidad (community/)

| Carpeta | Propósito | Permisos |
|---------|-----------|----------|
| `agents/` | Agentes creados por usuarios | Escritura (con PR) |
| `tools/` | Herramientas auxiliares | Escritura (con PR) |
| `integrations/` | Integraciones con sistemas | Escritura (con PR) |
| `primitives/` | Primitivas propuestas | Escritura (con PR) |

### Scripts (scripts/)

| Archivo | Lenguaje | Función |
|---------|----------|---------|
| `check_license_eligibility.py` | Python 3 | Verifica elegibilidad según umbrales PYME |

**Características:**
- Modo interactivo
- Modo CLI con argumentos
- Output JSON opcional
- Reporte formateado

### Recursos del Libro (libro/)

| Archivo | Contenido |
|---------|-----------|
| `insercion_enlace.txt` | Texto completo para insertar en el libro con QR |

**Incluye:**
- Texto largo (página completa)
- Texto corto (espacio limitado)
- Instrucciones para generar QR
- Guía para diseñador

---

## 🔒 Permisos por Carpeta

| Carpeta | Propietario | Contribuyentes | Comunidad |
|---------|-------------|----------------|-----------|
| `core/` | @salvadorferrer | Solo lectura | Solo lectura |
| `docs/` | @maintainers | PR requerido | PR requerido |
| `community/` | @maintainers | PR requerido | PR requerido |
| `scripts/` | @maintainers | PR requerido | PR requerido |
| Raíz | @salvadorferrer | Solo lectura | Solo lectura |

---

## 📊 Estadísticas del Paquete

| Métrica | Valor |
|---------|-------|
| Archivos generados | 25+ |
| Líneas de documentación | 5,000+ |
| Idiomas | Español, Inglés |
| Formatos | Markdown, JSON, YAML, Python |

---

## ✅ Checklist de Archivos Completos

### Esenciales (Bloqueantes)

- [x] LICENSE
- [x] LICENSE-COMMERCIAL
- [x] README.md
- [x] core/SYSTEM_PROMPT_CORE_v5_CORREGIDO-v1.md
- [x] core/cognitive_primitives_atlas.json
- [x] core/libro_maestro_conocimiento_pedagogico.yml
- [x] core/libro_maestro_conocimiento_tecnico.yml
- [x] core/Operador de Enlace para METAFORGE.md

### Importantes (No bloqueantes)

- [x] CHANGELOG.md
- [x] CODE_OF_CONDUCT.md
- [x] CONTRIBUTING.md
- [x] SECURITY.md
- [x] docs/guia_uso.md
- [x] docs/github_setup_guide.md
- [x] PLAN_DE_ACCION.md

### Comunidad

- [x] community/agents/README.md
- [x] community/agents/PLANTILLA_README.md
- [x] community/tools/README.md

### Utilidades

- [x] scripts/check_license_eligibility.py
- [x] libro/insercion_enlace.txt

---

## 📝 Notas para el Usuario

1. **Archivos marcados como [Por crear]** deben ser generados según necesidad
2. **Archivos marcados como [Por poblar]** requieren contenido adicional
3. Los archivos en `core/` son **SOLO LECTURA** para la comunidad
4. Todas las contribuciones deben pasar por **Pull Request**

---

<div align="center">

**[⬆ Volver al inicio](#índice-de-archivos-generados---meta-forge-v5)**

*Última actualización: 2026-02-18*

</div>
