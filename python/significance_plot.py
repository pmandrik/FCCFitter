import json
import optparse
import sys
from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import os

#__________________________________________________________
def getMassDisco(signiDict):
    
    indict=None
    with open(signiDict,'r') as f:
        indict = json.load(f)
        
    mass =[]
    disco = []

    for m in indict:
        signi=[]
        lumi=[]
        print m
        for i in indict[m]:
            signi.append(i['signi'])
            lumi.append(i['lumi'])
        print signi
        print lumi

        signi,lumi = zip(*sorted(zip(signi, lumi)))

        plt.figure()
        xnew = np.linspace(min(lumi), max(lumi), 100)
        f = interp1d(lumi, signi)
        plt.plot(lumi, signi, 'o-', xnew, f(xnew), '-')
        plt.plot([min(lumi), max(lumi)], [5, 5], 'k-', lw=2)
        plt.plot([min(lumi), max(lumi)], [3, 3], 'k-', lw=2)            
        plt.xlabel('luminosity fb$^{-1}')
        plt.ylabel('significance sigma')
        plt.grid(True)
        plt.savefig('Plots/Signi_%s.eps'%(m))
        plt.close()


        plt.figure()
        xnew = np.linspace(min(signi), max(signi), 1000)
        f = interp1d(signi, lumi)
        plt.plot(signi, lumi, 'o-', xnew, f(xnew), '-')
        plt.plot([5,5],[min(lumi), max(lumi)], 'k-', lw=2)
        plt.plot([3,3],[min(lumi), max(lumi)], 'k-', lw=2)            
        plt.ylabel('luminosity fb$^{-1}')
        plt.xlabel('significance sigma')
        plt.grid(True)
        discolumi = f(5) if xnew[-1]>5.0 else f(xnew[-1])
        plt.plot([0,5],[discolumi, discolumi], 'k-', lw=2)            
        plt.savefig('Plots/SigniInverse_%s.eps'%(m))
        print 'lumi = %f'%discolumi
        plt.close()

        mass.append(int(m))
        disco.append(discolumi)

    Mass,Disco = zip(*sorted(zip(mass, disco)))
    print Mass
    print Disco
    return Disco,Mass

#__________________________________________________________
if __name__=="__main__":
    
    parser = optparse.OptionParser(description="analysis parser")
    parser.add_option('-f', '--files', dest='files', type=str, default='')
    parser.add_option('-n', '--names', dest='names', type=str, default='')
    parser.add_option('-p', '--plot', dest='plot', type=str, default='')

    
    ops, args = parser.parse_args()
    signiDict=ops.files
    names=ops.names
    
    if not os.path.isdir("Plots/"):
        os.system('mkdir Plots')

    signiList = signiDict.split(' ')
    namesList = names.split(' ')
    print signiList
    print namesList
    if len(signiList)!=len(namesList):
        print 'different length, name, signi, exit',len(signiList),'  ',len(namesList)
        sys.exit(3)
    plt.figure()
    
    for s in xrange(len(signiList)):
        print signiList[s]
        Disco,Mass=getMassDisco(signiList[s])
        Disco=[i/1000. for i in Disco]
        from scipy import interpolate
        f = interpolate.interp1d(Mass, Disco)
        xnew = np.linspace(Mass[0],Mass[-1],50)
        Disco_smooth = f(xnew)

        plt.plot(Mass, Disco, label=namesList[s])
        #plt.plot( xnew, Disco_smooth, '-')
        


    plt.ylabel('Int. Luminosity fb$^{-1}$')
    plt.xlabel('mass [TeV]')
    #plt.title('luminosity verus mass for a 5 $\sigma$ discovery')
    if 'tt' in namesList:
        plt.ylim(ymax = 1000000, ymin = 100)
        plt.text(10.57, 500000, r'$Z\' \rightarrow = t \bar{t}$')
        plt.text(10.57, 300000, r'Integrated luminosity verus mass for a 5 $\sigma$ discovery')

        plt.text(10.57, 2500, r'$2.5ab^{-1}$')
        plt.plot([10,30], [2500, 2500], color='black')
        plt.text(10.57, 30000, r'$30ab^{-1}$')
        plt.plot([10,30], [30000, 30000], color='black')

    if 'll' in namesList:
        plt.ylim(ymax = 1000000, ymin = 10)
        plt.text(16, 500000, r'$Z\' \rightarrow = l^{+}l^{-}$')
        plt.text(16, 300000, r'Integrated luminosity verus mass for a 5 $\sigma$ discovery')

        plt.text(16, 2500, r'$2.5ab^{-1}$')
        plt.plot([15,50], [2500, 2500], color='black')
        plt.text(16, 30000, r'$30ab^{-1}$')
        plt.plot([15,50], [30000, 30000], color='black')
        plt.legend(loc=4)


    plt.grid(True)
    #plt.legend(loc=4)
    plt.yscale('log')

    plt.savefig('Plots/DiscoveryPotential_%s.eps'%(ops.plot))
    plt.savefig('Plots/DiscoveryPotential_%s.png'%(ops.plot))

    plt.close()




