import google.ai.generativelanguage as glm

product_profile_properties = {
    "name": glm.Schema(type=glm.Type.STRING, description="Combination of brand name and product name."),
    "proprietary_claims": glm.Schema(
        type=glm.Type.ARRAY, 
        items=glm.Schema(type=glm.Type.STRING)
    ),
    # "ingredients": glm.Schema(type=glm.Type.STRING),
    "ingredients": glm.Schema(
        type=glm.Type.ARRAY, 
        items=glm.Schema(type=glm.Type.STRING)
    ),
    "serving_size": glm.Schema(type=glm.Type.STRING),  # Serving size (e.g., "200g" or "1 packet")
    # "nutritional_information": glm.Schema(
    #     type=glm.Type.OBJECT,
    #     properties={
    #         "calories": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "fat": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "saturated_fat": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "monounsaturated_fat": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "polyunsaturated_fat": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "trans_fat": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "cholesterol": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "sodium": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "carbohydrates": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "dietary_fiber": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "total_sugar": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "added_sugar": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "protein": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "vitamin_a": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "vitamin_c": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "calcium": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         ),
    #         "iron": glm.Schema(
    #             type=glm.Type.OBJECT,
    #             properties={
    #                 "per_100g": glm.Schema(type=glm.Type.NUMBER),
    #                 "%_RDA": glm.Schema(type=glm.Type.NUMBER),
    #                 "unit": glm.Schema(type=glm.Type.STRING)
    #             }
    #         )
    #     }
    # )
    "nutritional_information": glm.Schema(
        type=glm.Type.ARRAY, 
        items=glm.Schema(type=glm.Type.STRING)
    )
}

product_profile = glm.Schema(
    type=glm.Type.OBJECT,
    properties=product_profile_properties,
    required=['name', 'proprietary_claims', 'ingredients', 'serving_size', 'nutritional_information']
)

get_product_profile = glm.FunctionDeclaration(
    name="get_product_profile",
    description="Get product profile with product name, proprietary claims made, ingredients, serving size, and detailed nutritional info.",
    parameters=glm.Schema(
        type=glm.Type.OBJECT,
        properties={
            "product": product_profile
        }
    )
)