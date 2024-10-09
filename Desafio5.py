interruptores = {"Interruptor 1": False, "Interruptor 2": False, "Interruptor 3": False}
lampadas = {"Lâmpada 1": {"estado": "desligada", "quente": False},
            "Lâmpada 2": {"estado": "desligada", "quente": False},
            "Lâmpada 3": {"estado": "desligada", "quente": False}}

interruptores["Interruptor 1"] = True
lampadas["Lâmpada 1"]["estado"] = "ligada"
lampadas["Lâmpada 1"]["quente"] = True

interruptores["Interruptor 1"] = False
lampadas["Lâmpada 1"]["estado"] = "desligada"
interruptores["Interruptor 2"] = True
lampadas["Lâmpada 2"]["estado"] = "ligada"

print("Estado das lâmpadas ao entrar na sala:")
for i, lampada in enumerate(lampadas, 1):
    estado = lampadas[lampada]["estado"]
    quente = "quente" if lampadas[lampada]["quente"] else "fria"
    print(f"Lâmpada {i}: {estado}, {quente}")

lampada_acessa = [lamp for lamp, info in lampadas.items() if info["estado"] == "ligada"]
lampada_quente = [lamp for lamp, info in lampadas.items() if info["quente"] and info["estado"] == "desligada"]
lampada_fria = [lamp for lamp, info in lampadas.items() if not info["quente"] and info["estado"] == "desligada"]

print("\nIdentificação dos interruptores:")
print(f"O Interruptor 1 controla {lampada_quente[0]}.")
print(f"O Interruptor 2 controla {lampada_acessa[0]}.")
print(f"O Interruptor 3 controla {lampada_fria[0]}.")