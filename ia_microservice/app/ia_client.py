import json
import openai

def analizar_con_ia(numero_cotizacion, precio, fecha, nombre_cliente, email, tipo_servicio, descripcion):
    prompt = f"""
    Analiza el siguiente caso legal y responde SOLO en formato JSON con las siguientes claves:
    - complejidad (Baja/Media/Alta)
    - ajuste_precio (0, 25, 50)
    - servicios_adicionales (lista de strings)
    - propuesta_texto (string, 2-3 párrafos profesionales)

    Datos de la cotización:
    - Número de cotización: {numero_cotizacion}
    - Nombre del cliente: {nombre_cliente}
    - Correo electrónico: {email}
    - Tipo de servicio: {tipo_servicio}
    - Descripción del caso: {descripcion}
    - Precio base sugerido: S/ {precio}
    - Fecha de solicitud: {fecha}
    """

    client = openai.OpenAI()
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=700
        )
        texto = response.choices[0].message.content

        try:
            data = json.loads(texto)
            return data
        except Exception:
            return {
                "complejidad": "Desconocido",
                "ajuste_precio": 0,
                "servicios_adicionales": [],
                "propuesta_texto": texto
            }
    except openai.AuthenticationError:
        return {
            "complejidad": "Error",
            "ajuste_precio": 0,
            "servicios_adicionales": [],
            "propuesta_texto": "API key de OpenAI incorrecta o inválida. Verifica tu clave en el archivo .env."
        }
    except openai.RateLimitError:
        return {
            "complejidad": "Error",
            "ajuste_precio": 0,
            "servicios_adicionales": [],
            "propuesta_texto": "No tienes más tokens gratuitos o has superado el límite de uso de la API de OpenAI. Por favor, revisa tu cuenta."
        }
    except Exception as e:
        return {
            "complejidad": "Error",
            "ajuste_precio": 0,
            "servicios_adicionales": [],
            "propuesta_texto": f"Error inesperado: {str(e)}"
        }