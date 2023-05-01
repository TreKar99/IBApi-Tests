from ibapi.client import *
from ibapi.wrapper import *
import time

# PASOS PREVIOS
# 1. Abrir TWS
# 2. Habilitar sockets (port: 7497)
# 3. Run

# App: contiene el Cliente y el Wrapper
class App(EClient, EWrapper):
    # Constructor
    def __init__(self):
        EClient.__init__(self, self)

    # Detalles Contrato
    def contractDetails(self, reqId, contractDetails):
        print(f"Detalles contrato: {contractDetails.longName}")

    # Fin Detalles Contrato
    def contractDetailsEnd(self, reqId: int):
        print("Fin de detalles contrato")
        self.disconnect()

    # Error Handling
    def error(self, reqId, errorCode, errorString):
        # 502: Error Socket
        if(errorCode == 502): pass
        # 504: NO conexión
        elif(errorCode == 504): print("Fallo de conexión")
        elif(errorCode not in self.goodErrors): print("Error {} {} {}".format(reqId,errorCode,errorString))

    # Errores no importantes:
    # - 2104: Market Data Farm OK
    # - 2106: Historical Data Farm OK
    # - 2158: Sec-Def Data Farm OK
    goodErrors = (2104, 2106, 2158)


def main():
    
    app = App()

    app.connect("127.0.0.1", 7497, 1000)    # Socket a TWS (Paper trading port: 7497)
    time.sleep(1)                           # Espera para conectar socket.

    mycontract = Contract()                 # CONTRATO = TÍTULO = QUE BUSCAS
    mycontract.symbol = "AMZNa"
    mycontract.secType = "STK"
    mycontract.exchange = "SMART"
    mycontract.currency = "USD"
    mycontract.primaryExchange = "ISLAND"
            
    app.reqContractDetails(1, mycontract)

    app.run()
    
if __name__ == "__main__":
    main()
