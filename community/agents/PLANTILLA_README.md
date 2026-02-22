# Plantilla README para Agentes de Comunidad

> Copia este archivo como `README.md` en la carpeta de tu agente y completa la información.

---

# [Nombre del Agente]

## 📝 Descripción

Breve descripción de qué hace el agente y su propósito principal.

**Ejemplo:**
> Agente especializado en análisis de contratos legales que identifica cláusulas abusivas, riesgos potenciales y oportunidades de negociación.

---

## 🎯 Dominio

- **Categoría:** [Legal / HR / Fintech / Healthcare / Manufacturing / Cybersecurity / Otro]
- **Sub-dominio:** [Especificar área específica]
- **Nivel de especialización:** [Generalista / Especialista / Experto]

---

## ✅ Requisitos

### Modelo LLM Recomendado
- **Primera opción:** [GPT-4o / Claude 3.5 Sonnet / Gemini 1.5 Pro / Otro]
- **Mínimo aceptable:** [Modelo mínimo recomendado]
- **Context window:** [Tokens mínimos requeridos]

### Herramientas Necesarias
- [ ] Web search
- [ ] Python sandbox
- [ ] Code interpreter
- [ ] Vision capabilities
- [ ] Otras: [Especificar]

### Archivos de Contexto Requeridos
- [ ] `libro_maestro_conocimiento_pedagogico.yml`
- [ ] `libro_maestro_conocimiento_tecnico.yml`
- [ ] `cognitive_primitives_atlas.json`
- [ ] Archivos adicionales: [Listar si aplica]

---

## 🚀 Uso

### Inicialización

```yaml
# Bloque de inicialización para el agente
INICIALIZAR_AGENTE_[NOMBRE]
[MODE]: [OPERATOR_DRIVEN / INTERACTIVE]
[PROFILE]: [PER_01_NOVATO / PER_02_EXPERTO]
```

### Input Esperado

Describe el formato de input que espera el agente:

```json
{
  "campo_obligatorio_1": "descripción",
  "campo_obligatorio_2": "descripción",
  "campo_opcional": "descripción"
}
```

### Output Generado

Describe el formato de output que genera:

```json
{
  "resultado": "...",
  "confianza": 0.95,
  "metadata": {...}
}
```

---

## 💡 Ejemplos

### Ejemplo 1: [Caso de Uso]

**Input:**
```
[Escribir ejemplo de input real]
```

**Output:**
```
[Escribir ejemplo de output esperado]
```

### Ejemplo 2: [Otro Caso de Uso]

**Input:**
```
...
```

**Output:**
```
...
```

---

## ⚠️ Limitaciones

### Qué NO puede hacer este agente

- [ ] Limitación 1
- [ ] Limitación 2
- [ ] Limitación 3

### Casos de uso no recomendados

- No usar para [caso específico]
- No confiar ciegamente para [tipo de decisión]
- Requiere validación humana para [tipo de output]

---

## 🔧 Configuración Avanzada

### Parámetros Ajustables

| Parámetro | Descripción | Default | Rango |
|-----------|-------------|---------|-------|
| `param_1` | Descripción | `valor` | [min-max] |
| `param_2` | Descripción | `valor` | [min-max] |

### Anclas de Conocimiento Utilizadas

- `[ANCLA_1]` - Descripción de uso
- `[ANCLA_2]` - Descripción de uso
- `[ANCLA_3]` - Descripción de uso

### Primitivas Cognitivas Aplicadas

- `[COGPROC_XXX]` - Propósito en este agente
- `[THSTR_XXX]` - Propósito en este agente

---

## 📊 Métricas de Rendimiento

### Precisión Estimada
- **Caso de uso A:** X%
- **Caso de uso B:** Y%

### Tasa de Alucinación
- Observada: Z%
- Condiciones: [Cuándo es más propenso]

### Costo Aproximado
- Tokens por consulta típica: [Número]
- Costo estimado (GPT-4): $[Monto] por consulta

---

## 🧪 Testing

### Casos de Prueba Incluidos

1. **Test básico:** [Descripción]
2. **Test de estrés:** [Descripción]
3. **Test de seguridad:** [Descripción]

### Cómo Ejecutar Tests

```bash
# Comando para ejecutar tests
python test_agent.py --agent [nombre]
```

---

## 📜 Licencia

Este agente se distribuye bajo: [Especificar licencia]

**Debe ser compatible con:**
- Licencia dual META FORGE v5 (Personal/Comercial)
- Términos de uso del modelo LLM subyacente

### Tipo de Licencia Recomendada

```
[ ] MIT License (más permisiva)
[ ] Apache 2.0 (con protección de patentes)
[ ] Creative Commons BY-SA 4.0 (para documentación)
[ ] Otra: [Especificar]
```

---

## 👤 Autor

- **Nombre:** [Tu nombre o alias]
- **GitHub:** [@tu_usuario](https://github.com/tu_usuario)
- **Email:** [tu@email.com] (opcional)
- **Web:** [tu-web.com] (opcional)

### Contribuidores

- [@usuario1](https://github.com/usuario1) - [Contribución]
- [@usuario2](https://github.com/usuario2) - [Contribución]

---

## 🙏 Agradecimientos

- Salvador Ferrer Moncho por el sistema META FORGE v5
- [Otras personas o recursos a agradecer]

---

## 📚 Referencias

- [Enlace a documentación relevante]
- [Enlace a papers o recursos académicos]
- [Enlace a herramientas relacionadas]

---

## 🗺️ Roadmap

- [ ] Mejora 1 planificada
- [ ] Mejora 2 planificada
- [ ] Característica futura

---

<div align="center">

**[⬆ Volver al inicio](#nombre-del-agente)**

*Creado con [META FORGE v5](https://github.com/salvadorferrer/metaforge-v5)*

</div>
