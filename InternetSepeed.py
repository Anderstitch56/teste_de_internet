import speedtest
import PySimpleGUI as sg

sg.theme("Dark")
fonte = ("Helvetica", 12)

def telaInicial():
    
    
    layout = [
        [sg.Text("TESTE DE VELOCIDADE DE INTERNET")],
        [sg.Button("SAIR", key="sair", button_color=("white", "red")),
         sg.Button("INICIAR", key="iniciar", button_color=("white", "green"))],
    ]
    return sg.Window("TESTE DE VELOCIDADE DE INTERNET", layout=layout, finalize=True, element_justification="c", font=fonte)

def TelaTeste():
    layout = [
        [sg.Text("Velocidade de Download: "), sg.Text("", key="download")],
        [sg.Text("Velocidade de Upload: "), sg.Text("", key="upload")],
        [sg.Text("Ping: "), sg.Text("", key="ping")],
        [sg.Button("SAIR", key="sair", button_color=("white", "red")),
         sg.Button("VOLTAR", key="voltar", button_color=("white", "green"))],
    ]
    return sg.Window("TESTE DE VELOCIDADE DE INTERNET", layout=layout, finalize=True, font=fonte)

def medir_velocidade(janela):
    try:
        sg.popup_no_buttons("Tentando conectar com a internet, aguarde...", auto_close=True, auto_close_duration=4)

        st = speedtest.Speedtest()
        st.get_best_server()

        download_speed = st.download() / 1_000_000  # Convertendo para Mbps
        upload_speed = st.upload() / 1_000_000  # Convertendo para Mbps
        ping = st.results.ping

        janela["download"].update(f"{download_speed:.2f} Mbps")
        janela["upload"].update(f"{upload_speed:.2f} Mbps")
        janela["ping"].update(f"{ping:.2f} ms")

    except speedtest.ConfigRetrievalError:
        sg.popup("Erro ao obter configuração do servidor.")
    except speedtest.SpeedtestException:
        sg.popup("Não foi possível realizar o teste. Verifique sua conexão com a internet.")
    except Exception as e:
        sg.popup(f"Erro inesperado: {e}")

janela1, janela2 = telaInicial(), None

while True:
    window, event, values = sg.read_all_windows()

    if event == "sair" or event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == "iniciar":
        janela1.hide()
        janela2 = TelaTeste()
        medir_velocidade(janela2)

    elif window == janela2 and event == "voltar":
        janela2.close()
        janela1.un_hide()
