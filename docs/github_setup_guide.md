# ============================================================================
# AUTHOR_IDENTITY_BLOCK [ROOT_ACCESS_ONLY]
# ============================================================================
# IDENTIFIER:  Salvador Ferrer
# PROJECT:     METAFORGE_v5 (Community Tools Registry)
# BOOK_REF:    "CÓMO CONSTRUIR AGENTES DE IA QUE NO ALUCINAN"
# STATUS:      COMMUNITY_GATEWAY_ACTIVE
# ============================================================================

# Guía de Configuración de GitHub para METAFORGE v5

> Configuración recomendada para proteger los activos del proyecto.

---

## 📋 Índice

1. [Configuración Inicial del Repositorio](#configuración-inicial)
2. [Protección de Ramas](#protección-de-ramas)
3. [Permisos de Equipos](#permisos-de-equipos)
4. [Configuración de Seguridad](#configuración-de-seguridad)
5. [Automatizaciones](#automatizaciones)

---

## Configuración Inicial

### 1. Crear el Repositorio

```bash
# Crear repositorio en GitHub
# Nombre recomendado: metaforge-v5
# Visibilidad: Público
# Inicializar con: README.md
```

### 2. Estructura de Carpetas

```
metaforge-v5/
├── community/              # Contribuciones de agentes y herramientas
├── core/                   # Kernel, Navigator y Anclas (Solo Lectura)
├── docs/                   # Guías, manuales y activos visuales
├── libro/                  # Referencias al manuscrito original
├── scripts/                # Validadores de licencia y sincronización
├── CHANGELOG.md            # Historial de versiones
├── LICENSE                 # Licencia Dual (Personal/Comercial)
└── README.md               # Puerta de enlace al sistema
```

### 3. Archivos Iniciales Requeridos

- [ ] LICENSE
- [ ] LICENSE-COMMERCIAL
- [ ] README.md
- [ ] CHANGELOG.md
- [ ] CODE_OF_CONDUCT.md
- [ ] CONTRIBUTING.md
- [ ] SECURITY.md

---

## Protección de Ramas

### Rama `main` (Protegida)

Configuración recomendada:

```yaml
# .github/settings.yml (usando Probot Settings)
branches:
  - name: main
    protection:
      required_pull_request_reviews:
        required_approving_review_count: 1
        dismiss_stale_reviews: true
        require_code_owner_reviews: true
      required_status_checks:
        strict: true
        contexts:
          - "continuous-integration"
      enforce_admins: true
      restrictions:
        users: []
        teams: []
```

### Pasos para Configurar

1. **Ir a Settings > Branches**

2. **Añadir regla para `main`:**
   - ☑️ Require a pull request before merging
   - ☑️ Require approvals (mínimo 1)
   - ☑️ Dismiss stale PR approvals
   - ☑️ Require review from CODEOWNERS
   - ☑️ Require status checks to pass
   - ☑️ Include administrators

3. **Ramas adicionales protegidas:**
   - `release/*`
   - `core/*`

---

## Permisos de Equipos

### Estructura de Equipos

```
metaforge-v5/
├── @maintainers        # Control total
├── @core-contributors  # Pueden proponer cambios a core/
├── @community-mods     # Revisan contribuciones
└── @contributors       # Solo lectura + PRs
```

### Permisos por Carpeta (CODEOWNERS)

```
# .github/CODEOWNERS

# Activos principales - solo mantenedores
/core/*                     @salvadorferrer @maintainers
/SYSTEM_PROMPT_CORE_v5.md   @salvadorferrer
/cognitive_primitives_atlas.json  @salvadorferrer
/libro_maestro_conocimiento_*.yml @salvadorferrer

# Documentación - mantenedores y contribuidores
/docs/*                     @maintainers @core-contributors

# Community - más permisivo
/community/*                @maintainers @community-mods @core-contributors

# Scripts - revisión técnica requerida
/scripts/*                  @maintainers @core-contributors

# Raíz - solo mantenedores
/*                          @salvadorferrer @maintainers
```

### Configuración de Permisos

| Rol | Permisos | Descripción |
|-----|----------|-------------|
| **Admin** | Todo | Propietario del repositorio |
| **Maintain** | Casi todo | Mantenedores principales |
| **Write** | Push, PR | Contribuidores de confianza |
| **Triage** | Issues, PRs | Moderadores de comunidad |
| **Read** | Solo lectura | Contribuidores generales |

---

## Configuración de Seguridad

### Security Advisories

1. **Habilitar en:** Settings > Security > Code security

2. **Configuración:**
   - ☑️ Private vulnerability reporting
   - ☑️ Dependabot alerts
   - ☑️ Dependabot security updates
   - ☑️ Secret scanning

### Archivo SECURITY.md

Ya incluido en el paquete. Verifica que incluya:
- Email de contacto: security@metaforge.ai
- Proceso de divulgación responsable
- Tiempo de respuesta esperado (48h)

### Política de Seguridad

```yaml
# .github/security.md (configuración adicional)
security:
  enable_vulnerability_reporting: true
  contact_email: security@metaforge.ai
  response_time: "48 hours"
  disclosure_policy: "90 days responsible disclosure"
```

---

## Automatizaciones

### GitHub Actions

#### 1. Validación de PRs

```yaml
# .github/workflows/validate-pr.yml
name: Validate Pull Request

on:
  pull_request:
    paths:
      - 'community/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Check PR template
        run: |
          # Verificar que sigue la plantilla
          
      - name: Validate JSON/YAML
        run: |
          # Validar sintaxis de archivos
          
      - name: Check license compatibility
        run: |
          # Verificar licencia compatible
```

#### 2. Protección de Archivos Core

```yaml
# .github/workflows/protect-core.yml
name: Protect Core Files

on:
  pull_request:
    paths:
      - 'core/**'
      - 'SYSTEM_PROMPT_CORE_v5.md'
      - 'cognitive_primitives_atlas.json'
      - 'libro_maestro_conocimiento_*.yml'

jobs:
  block-core-changes:
    runs-on: ubuntu-latest
    steps:
      - name: Block changes to core files
        run: |
          echo "❌ Los archivos core/ son de solo lectura para la comunidad."
          echo "Contacta a @salvadorferrer para cambios en archivos core."
          exit 1
```

#### 3. Bienvenida a Contribuyentes

```yaml
# .github/workflows/welcome.yml
name: Welcome Contributors

on:
  pull_request:
    types: [opened]

jobs:
  welcome:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/first-interaction@v1
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
          pr-message: |
            ¡Gracias por tu contribución a METAFORGE v5! 🎉
            
            Un mantenedor revisará tu PR en los próximos 7 días.
            
            Mientras tanto:
            - Asegúrate de haber leído CONTRIBUTING.md
            - Verifica que tu código pasa las validaciones
            - Responde a cualquier feedback constructivo
```

### Plantillas de Issues

#### Bug Report

```markdown
<!-- .github/ISSUE_TEMPLATE/bug_report.md -->
---
name: Reportar Bug
about: Crea un reporte de bug
---

**Descripción del bug**
Descripción clara del problema.

**Pasos para reproducir**
1. Ir a '...'
2. Click en '...'
3. Ver error

**Comportamiento esperado**
Qué debería pasar.

**Entorno:**
- Modelo LLM: [ej. GPT-4o]
- Versión: [ej. 5.0.0]
- Entorno: [ej. Cloud/Local]
```

#### Feature Request

```markdown
<!-- .github/ISSUE_TEMPLATE/feature_request.md -->
---
name: Solicitud de Feature
about: Sugiere una nueva característica
---

**¿Tu feature resuelve un problema?**
Descripción del problema.

**Describe la solución deseada**
Qué te gustaría que pasara.

**Describe alternativas consideradas**
Otras soluciones posibles.

**Contexto adicional**
Cualquier otro contexto.
```

### Plantilla de Pull Request

```markdown
<!-- .github/PULL_REQUEST_TEMPLATE.md -->

## Descripción
Breve descripción de los cambios.

## Tipo de cambio
- [ ] Bug fix
- [ ] Nueva característica
- [ ] Documentación
- [ ] Refactorización

## Checklist
- [ ] He leído CONTRIBUTING.md
- [ ] Mi código sigue las guías de estilo
- [ ] He añadido tests si aplica
- [ ] La documentación está actualizada

## Área afectada
- [ ] community/agents
- [ ] community/tools
- [ ] community/primitives
- [ ] docs
- [ ] scripts
```

---

## Configuración de Releases

### Versionado Semántico

```
MAJOR.MINOR.PATCH

Ejemplo: 5.0.0
- MAJOR (5): Cambios incompatibles
- MINOR (0): Nuevas características
- PATCH (0): Correcciones de bugs
```

### Crear un Release

1. **Crear tag:**
   ```bash
   git tag -a v5.0.0 -m "Release v5.0.0 - Industrial"
   git push origin v5.0.0
   ```

2. **Crear release en GitHub:**
   - Ir a Releases > Draft new release
   - Seleccionar tag
   - Título: "METAFORGE v5.0.0 - Industrial"
   - Descripción: Copiar desde CHANGELOG.md

3. **Assets:**
   - Código fuente (zip)
   - Código fuente (tar.gz)
   - [Opcional] Paquete pre-compilado

---

## Checklist de Configuración

### Antes de Publicar

- [ ] Repositorio creado y configurado
- [ ] Archivos base subidos
- [ ] LICENSE y LICENSE-COMMERCIAL incluidos
- [ ] Rama main protegida
- [ ] CODEOWNERS configurado
- [ ] Plantillas de Issues/PRs creadas
- [ ] GitHub Actions configuradas
- [ ] Seguridad habilitada
- [ ] README.md completo
- [ ] Primer release creado

### Después de Publicar

- [ ] Invitar a mantenedores
- [ ] Configurar notificaciones
- [ ] Anunciar en redes sociales
- [ ] Monitorear issues
- [ ] Responder a contribuciones

---

## Comandos Útiles

```bash
# Configurar git local
git config user.name "Tu Nombre"
git config user.email "tu@email.com"

# Clonar repositorio
git clone https://github.com/salvadorferrer/metaforge-v5.git

# Crear rama de trabajo
git checkout -b feature/nueva-caracteristica

# Subir cambios
git add .
git commit -m "Add: descripción clara"
git push origin feature/nueva-caracteristica

# Sincronizar con main
git checkout main
git pull origin main
```

---

<div align="center">

**[⬆ Volver al inicio](#guía-de-configuración-de-github)**

*Para soporte: support@metaforge.ai*

</div>
