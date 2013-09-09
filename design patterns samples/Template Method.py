#!/usr/bin/python

'''
    Criado e testado no http://repl.it/
	Feito melhor em : http://www.dofactory.com/Patterns/PatternTemplate.aspx
'''
class NfeTemplate:
        
    def GetHeader(self):
        return "default header"
        
    def GetItems(self):
        return "default items"
        
    def GetFooter(self):
        return "default footer"
        

    # Mais conhecido como Run
    def GiveMeTheNFEBitch(self):
        nfe = """
Here is your NFE mester!
        {0}
        {1}
        {2}
""".format(self.GetHeader(),self.GetItems(), self.GetFooter())

        return nfe


        
class NfeTypeXXX(NfeTemplate):
    def GetHeader(self):
        return self.__class__.__name__+"- header"
        
    def GetItems(self):
        return self.__class__.__name__+"- items"
        
    def GetFooter(self):
        return self.__class__.__name__+"- footer"
        
class NfeTypeYYY(NfeTemplate):
    def GetHeader(self):
        return self.__class__.__name__+"- header"
        
    def GetItems(self):
        return self.__class__.__name__+"- items"
        
    def GetFooter(self):
        return self.__class__.__name__+"- footer"        
              

class NFePrinter:
    '''
        Classe para imprimir os dados da NFE no console
    '''

    '''
        Decide qual template vai usar.
        - Criei apenas 3 tipos:
           - default: 1; 
           - XXX: 2: e o 
           - YYY.
        Informa um dos 3 números para selecionar o tipo da nota que deseja 
        imprimir
    '''
    tplSelected = 1
    tplInstanceSelected = NfeTemplate()

        
    def __init__(self, templateSelected):
        self.tplSelected = templateSelected
        
        '''
        Seleciona o template no dicionario.
        - Aqui você pode criar várias implementação de NfeTemplate,
        uma implementação para cada tipo de NFE, como o fluxo é sempre o mesmo
        o builder constrói a nfe para você, você só se preocupa com o passos da
        construção e não mais com a ordem do que está sendo implementado.
        '''
        self.tplInstanceSelected = {
                1:NfeTemplate(),
                2:NfeTypeXXX(),
                3:NfeTypeYYY()
            }[self.tplSelected]
        
        print "template selecionado:" + self.tplInstanceSelected.__class__.__name__
        
    
    def PrintRightNow(self):
        # cria o builder.
        template = self.tplInstanceSelected

        # obtém a nfe.
        result = template.GiveMeTheNFEBitch()
        
        # imprime a nfe.
        print result

# Não funcionou no http://repl.it/
# tpl = raw_input("Informe 1,2 ou 3 - qualquer outro valor não garanto")
tpl = 2 # << informa o template aqui para o teste

NFePrinter(tpl).PrintRightNow()

