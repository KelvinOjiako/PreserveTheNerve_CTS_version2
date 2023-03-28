class MenuOptons:
    def __int__(self):
        pass

    def gui_user_menu(self, user_choice):
        switch_cases = {
            0: "Performs Serial Communication with Arduino and begins the Shocking with Tens Unit" +
               "Arduino will then relay the information back to Raspberry pi",
            1: "Performs Additional Filtering and Amplification on signal gotten from Arduino",
            2: "Statistical methods to optimize signal and extrapolate the necessary variables from the signal",
            3: "Performs a Medical Diagnosis of the patient",
            4: "Calculates the Severity Level",
            5: "Exports the information to an external file"
        }

        return switch_cases.get(user_choice)

