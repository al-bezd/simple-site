'''from wagtail.core import hooks
@hooks.register("register_rich_text_features")
def register_colortext_feature(features):
    """Creates centered text in our richtext editor and page."""

    # Step 1
    feature_name = "Text Color Picker"
    type_ = "TEXTCOLOR"
    tag = "span"

    # Step 2
    control = {
        "type": type_,
        "label": "color",
        "description": "Color Text",
        # "style": {
        #     "display": "block",
        #     "text-align": "center",
        # },
    }

    # Step 3
    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    # Step 4
    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {
            "style_map": {
                type_: {
                    "element": tag,
                    "props": {
                        "style": "color:colorcode"
                    }
                }
            }
        }
    }

    # Step 5
    features.register_converter_rule("contentstate", feature_name, db_conversion)

    # Step 6, This is optional.
    features.default_features.append(feature_name)'''