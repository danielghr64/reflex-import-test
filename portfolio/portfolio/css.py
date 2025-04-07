
styles = {
    "main":{
        "property":{
            "width": "100%",
            "height": "75vh",
            "padding": "10rem 0rem",
            "align_items": "center",
            "justify_content": "start"
        }
    },
    "dots": {
        "@keyframes dots": {
            "0%": {"background_position": "0 0"},
            "100%": {"background_position": "40px 40px"}
        },
        "animation": "dots 4s linear infinite alternate-reverse both"
    },
    "wave": {
        "@keyframes wave": {
            "0%": {"transform": "rotate(45deg)"},
            "100%": {"transform": "rotate(-20deg)"}
        },
        "animation": "wave 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) infinite alternate-reverse both"
    },
    "footer": {
        "width": ["100%", "90%", "60%", "45%", "45%"],
        "height": "50px",
        "align_items": "center",
        "justify_content": "center"
    }
}
