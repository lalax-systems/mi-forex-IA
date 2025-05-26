# Política de Seguridad

## Versiones Soportadas

Este es un proyecto educativo en desarrollo activo. No ofrecemos soporte para versiones específicas.

| Versión | Soporte          |
|---------|------------------|
| Todas   | 🔴 No soportadas |

## Reporte de Vulnerabilidades

Si descubres una vulnerabilidad de seguridad:

1. **No la divulgues públicamente**
2. Contacta inmediatamente a [info@lalax.com] con:
   - Descripción detallada de la vulnerabilidad
   - Pasos para reproducirla
   - Impacto potencial estimado

**Tiempo de respuesta**: 72 horas hábiles para confirmación y evaluación inicial.

## Buenas Prácticas de Seguridad

1. **Uso educativo exclusivo**: Este software no debe usarse con fondos reales
2. **Protección de credenciales**:
   - Nunca commits credenciales API en el código
   - Usa variables de entorno para datos sensibles
3. **Verificación de datos**: Valida siempre los inputs de fechas/tickers
4. **Dependencias**: Actualiza regularmente con `pip check`