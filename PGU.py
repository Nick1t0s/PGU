import pygame


class pgButton:
    def __init__(self,surface,xy,height,width,function,args=[],changeXYWH=False,backGround=None,text=None,textColor=(0,0,0),font=None,smooth=True,pict=None,
                 pressXY=None,pressHeight=None,pressWidth=None,pressBackground=None,pressText=None,pressTextColor=None,pressFont=None,
                 pressSmooth=True,pressPict=None):
        self.surface=surface
        self.xy=xy
        self.height=height
        self.width=width
        self.bg=backGround
        self.text=text
        self.textCol=textColor
        self.font=font
        self.smooth=smooth
        self.pict=pict
        self.pXY=pressXY
        self.pHight=pressHeight
        self.pWidth=pressWidth
        self.pBg=pressBackground
        self.pText=pressText
        self.pTextCol=pressTextColor
        self.pFont=pressFont
        self.pSmoth=pressSmooth
        self.pPict=pressPict

        self.func=function
        self.args=args
        self.changeXYWH=changeXYWH

    def blit(self):
        if self.text != None:
            text = self.font.render(self.text, self.smooth, self.textCol)
            textR = text.get_rect(center=(self.xy[0] + self.width // 2, self.xy[1] + self.height // 2))
            if self.changeXYWH:
                print("dfsfd")
                if self.bg != None:
                    pygame.draw.rect(self.surface, self.bg, textR)
                self.xy=(textR.topleft)
                self.width=textR.width
                self.height=textR.height
            else:
                if self.bg != None:
                    pygame.draw.rect(self.surface, self.bg, (self.xy[0],self.xy[1],self.width,self.height))
            self.surface.blit(text, textR)
        elif self.pict != None:
            picTS=pygame.transform.scale(self.pict,(200,200))
            picTSRect=picTS.get_rect(topleft=self.xy)
            self.surface.blit(picTS,picTSRect)


