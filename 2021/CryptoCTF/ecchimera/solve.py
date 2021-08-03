from sage.all import *
from Crypto.Util.number import *

n = 43216667049953267964807040003094883441902922285265979216983383601881964164181
U = 18230294945466842193029464818176109628473414458693455272527849780121431872221
V = 13100009444194791894141652184719316024656527520759416974806280188465496030062
W = 5543957019331266247602346710470760261172306141315670694208966786894467019982

p = 190116434441822299465355144611018694747
q = 227316839687407660649258155239617355023

E1 = EllipticCurve(GF(p), [0,U,0,V,W])
G1 = E1(6907136022576092896571634972837671088049787669883537619895520267229978111036, 35183770197918519490131925119869132666355991678945374923783026655753112300226)
sG1= E1(14307615146512108428634858855432876073550684773654843931813155864728883306026, 4017273397399838235912099970694615152686460424982458188724369340441833733921)
E2 = EllipticCurve(GF(q), [0,U,0,V,W])
G2 = E2(6907136022576092896571634972837671088049787669883537619895520267229978111036, 35183770197918519490131925119869132666355991678945374923783026655753112300226)
sG2= E2(14307615146512108428634858855432876073550684773654843931813155864728883306026, 4017273397399838235912099970694615152686460424982458188724369340441833733921)

def SmartAttack(P,Q,p):     #https://crypto.stackexchange.com/questions/70454/why-smarts-attack-doesnt-work-on-this-ecdlp
     E = P.curve() 
     Eqp = EllipticCurve(Qp(p, 2), [ ZZ(t) + randint(0,p)*p for t in E.a_invariants() ]) 
  
     P_Qps = Eqp.lift_x(ZZ(P.xy()[0]), all=True) 
     for P_Qp in P_Qps: 
         if GF(p)(P_Qp.xy()[1]) == P.xy()[1]: 
             break 
  
     Q_Qps = Eqp.lift_x(ZZ(Q.xy()[0]), all=True) 
     for Q_Qp in Q_Qps: 
         if GF(p)(Q_Qp.xy()[1]) == Q.xy()[1]: 
             break 
  
     p_times_P = p*P_Qp 
     p_times_Q = p*Q_Qp 

     x_P,y_P = p_times_P.xy() 
     x_Q,y_Q = p_times_Q.xy() 

     phi_P = -(x_P/y_P) 
     phi_Q = -(x_Q/y_Q) 
     k = phi_Q/phi_P 
     return ZZ(k)

assert (E1.order() == p)
sp = SmartAttack(G1, sG1, p)
assert (E2.order() == 2**4 * 3 * 13 * 233 * 4253 * 49555349 * 7418313402470596923151)
sq = discrete_log(7418313402470596923151*sG2, 7418313402470596923151*G2, operation='+', bounds=[1,E2.order()//7418313402470596923151])
print(long_to_bytes(crt([sp, sq], [p, E2.order()//7418313402470596923151])))

#CCTF{m1X3d_VeR5!0n_oF_3Cc!}
