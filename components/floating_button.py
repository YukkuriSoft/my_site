import streamlit.components.v2 as components


def floating_button():
    CSS = """
    .float-button {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background-color: #ff4b4b;
        color: white;
        font-size: 24px;
        border: none;
        cursor: pointer;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
        z-index: 1000;
    }
    """
    HTML = '<button class="float-button">+</button>'
    JS = """
    export default function(component) {
        const { setTriggerValue, parentElement } = component;
        const btn = parentElement.querySelector("button.float-button");
        btn.onclick = () => {
            setTriggerValue("clicked", true);
        }
    }
    """
    # ここでコンポーネント登録
    floating_button = components.component(
        name="floating_button",
        html=HTML,
        css=CSS,
        js=JS,
    )

    return floating_button(on_clicked_change=lambda: None).clicked


