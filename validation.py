# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:52:48 2021

@author: NITISH
"""


from random import choice,uniform,sample as sam
import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from math import floor
n =1000 # number of agents
r = 0.5 # neighborhood radius
no_ldr=6
count=0
total_count=2128
region_count=10
region_step=10/region_count
no_rallies=6
rally_count=floor(total_count/no_rallies)

color=['None','red','cyan','lime','sienna','pink','gold','lavender','yellow','crimson','grey','darkblue','fuchsia','ivory','olive','azure','chocolate','teal','magenta','khaki']
bjp=0.242;jdu=0.194;rjd=0.304;cong=0.034;ljp=0.051;op=0.071;ind=0.104
party_code={'BJP':0,'JDU':1,'RJD':2,'CON':3,'LJP':4,'OPT':5,'IND':6}
party_name=['BJP','JDU','RJD','CON','LJP','OPT','IND']
class agent:
    pass
class leader:
    pass

def total(parameter):
    sum=0
    for i in parameter:
        sum+=parameter[i]
    
    return sum

def perct(attr,value):
    count=0
    global agents
    for ag in agents:
        if getattr(ag,attr) == value:
            count+=1
    return count,count/n



def initialize():
    global mat
    global agents
    global ldrs
    global supp_dist
    global visited
    global region
    global neighbor_map
    mat=[[1]*7 for _ in range(n)]
    ldrs=[]
    agents = []
    visited={}
    region=[[[] for k in range(region_count)] for i in range(region_count)]
    neighbor_map=[[[] for k in range(region_count)] for i in range(region_count)]
    
    def mapping_nbr():
        global neighbor_map
        for i in range(region_count):
            for j in range(region_count):
                if i-1 != -1 :
                    neighbor_map[i][j].append(str(i-1)+str(j))
                    if j-1 != -1:
                        neighbor_map[i][j].append(str(i-1)+str(j-1))
                    if ((j+1) % region_count) != 0:
                        neighbor_map[i][j].append(str(i-1)+str(j+1))
                if j-1 != -1:
                    neighbor_map[i][j].append(str(i)+str(j-1))
                if ((j+1) % region_count) != 0:
                    neighbor_map[i][j].append(str(i)+str(j+1))
                if ((i+1) % region_count) !=0 :
                    neighbor_map[i][j].append(str(i+1)+str(j))
                    if j-1 != -1:
                        neighbor_map[i][j].append(str(i+1)+str(j-1))
                    if ((j+1) % region_count) != 0:
                        neighbor_map[i][j].append(str(i+1)+str(j+1))
                    
                    
                        
                
    
    def allocation(population,attr,options):
          
        for ag in agents:
            if len(options) !=0:
                setattr(ag,attr,choice(options))
                key=getattr(ag,attr)
                population[key]=population[key]-1
                
                if population[key]== 0:
                    options.remove(str(key))
    
    option_party=['BJP_core','JDU_core','RJD_core','CON_core','BJP_med','JDU_med','RJD_med','CON_med','BJP_low','JDU_low','RJD_low','CON_low','OPT','IND','LJP_core','LJP_med','LJP_low']
    
    supp_dist={'BJP_core':round(0.2*bjp*n),'BJP_med':round(0.5*bjp*n),'BJP_low':round(0.3*bjp*n),
            'JDU_core':round(0.2*jdu*n),'JDU_med':round(0.5*jdu*n),'JDU_low':round(0.3*jdu*n),
            'RJD_core':round(0.2*rjd*n),'RJD_med':round(0.5*rjd*n),'RJD_low':round(0.3*rjd*n),
            'CON_core':round(0.2*cong*n),'CON_med':round(0.5*cong*n),'CON_low':round(0.3*cong*n),
            'LJP_core':round(0.2*ljp*n),'LJP_med':round(0.5*ljp*n),'LJP_low':round(0.3*ljp*n),
            'OPT':round(op*n),'IND':round(ind*n)}
    print(total(supp_dist))
    
    option_caste=['Upper','Yadav','Kurmi','OBC','SC','Muslims','ST']
    caste_dist={'Upper':round(0.16*n),'Yadav':round(0.174*n),'Kurmi':round(0.104*n),
            'OBC':round(0.232*n),'SC':round(0.183*n),'Muslims':round(0.138*n),'ST':round(0.009*n)}
    
    option_tv=['yes','no']
    tv_dist={'yes':round(0.83*0.181*n),'no':round((1-(0.83*0.181))*n)}
    
    option_phone=['simple','smart','no']
    phone_dist={'simple':round(0.479*n),'smart':round(0.274*n),'no':round(0.247*n)}
    
    option_radio=['yes','no']
    radio_dist={'yes':round(0.1*n),'no':round(0.9*n)}
    
    option_rally=['yes','no']
    rally_dist={'yes':round(0.18*n),'no':round(0.82*n)}
    
    
    option_leader=['BJP','JDU','RJD','CON','LJP','OPT']
    option_r=[0.6,0.6,0.55,0.5,0.45,0.45]

    option_target=[0.52*n,0.475*n,0.514*n,0.485*n,0.382*n,0.483*n]
    global target_phone
    target_phone=[round(0.479*0.193*n),round(0.479*0.141*n),round(0.479*0.157*n),round(0.479*0.12*n),round(0.479*0.112*n),round(0.479*0.137*n)]
    print('Expected=',[0.223,0.139,0.193,0.149,0.057,0.149])
    for i in range(n):
        ag = agent()
        ag.id=i
        ag.x =uniform(0.2,9.8)
        ag.y =uniform(0.2,9.8)
        ag.row=int(ag.x/region_step)
        ag.col=int(ag.y/region_step)
        region[ag.row][ag.col].append(ag)
        agents.append(ag)
        
    for i in range(no_ldr):
        ld=leader()
        ld.id=i
        ld.party=option_leader[i]
        ld.r=option_r[i]
        ld.target=option_target[i]
        visited['ldr'+str(ld.id)]=[]
        ld.x=uniform(0.2,9.8)
        ld.y=uniform(0.2,9.8)
        ld.row=int(ld.x/region_step)
        ld.col=int(ld.y/region_step)
        region[ld.row][ld.col].append(ld)
        ldrs.append(ld)
    
    
        
    allocation(supp_dist,'party',option_party) 
    allocation(caste_dist,'caste',option_caste)
    allocation(tv_dist,'tv',option_tv)
    allocation(phone_dist,'phone',option_phone)
    allocation(radio_dist,'radio',option_radio)
    allocation(rally_dist,'rally',option_rally)
    
    like_martrix()
    mapping_nbr()
    print(neighbor_map)
    global fig,ax0,ax1
    fig, (ax0) = plt.subplots(1,gridspec_kw={'width_ratios': [1]})
    fig, (ax1) = plt.subplots(1,gridspec_kw={'width_ratios': [1]})
    #ax0.set_xlim([-1, len(ledr)])
    #ax0.set_ylim([0, n])
    ax0.set_xlabel('Parties')
    ax0.set_ylabel('Supporters Ratio')
    ax0.set_xlabel('Parties')
    ax1.set_ylabel('Supporters Ratio')
    ax1.title.set_text('Vote Share')
    ax1.title.set_text('Vote Share')
    
    
def observe():
    global agents
    global ldrs
    cla()
    black = [ag for ag in agents]
    leaders = [ag for ag in ldrs]
    plt.scatter([ag.x for ag in black], [ag.y for ag in black],c='k',s=60)
    plt.scatter([ag.x for ag in leaders], [ag.y for ag in leaders],c='b',s=100)
    plt.show()
    axis([0,10,0,10])

    
   

    '''if count==1500:
        draw_bar(grp,ax0)'''
        
        
        
    
        
def like_martrix():
    global mat
    
    
    for ag in agents:
        pty=ag.party[0:3]
        pty_supp=ag.party[4:]
        ind1=ag.id
        ind2=party_code[pty]
        if pty_supp=='core':
            mat[ind1][ind2]=round(uniform(8.0,10.0),3)
            
        elif pty_supp=='med':
            mat[ind1][ind2]=round(uniform(5.0,7.9),3)
            
        elif pty_supp == 'low':
            mat[ind1][ind2]=round(uniform(3.0,4.9),3)
        else:
            mat[ind1][ind2]=round(uniform(3.0,10.0),3)
            
    
def position_update(agt,inc=0):
    region[agt.row][agt.col].remove(agt)
    if inc==0:
        agt.x,agt.y=uniform(0.0,10.0), uniform(0.0,10.0)
    else:
        agt.x,agt.y=agt.x+uniform(-inc,inc), agt.y+uniform(-inc,inc)
        boundary_check(agt)
    agt.row=int(agt.x/region_step)
    agt.col=int(agt.y/region_step)
    region[agt.row][agt.col].append(agt)
           
           
        
def door_interaction():
    for ld in ldrs:
        visit=visited['ldr'+str(ld.id)]
        
        possible_neighbors=region[ld.row][ld.col]
        for k in neighbor_map[ld.row][ld.col]:
            print(k)
            possible_neighbors+=region[int(k[0])][int(k[1])]
            print(possible_neighbors)
        neighbors = [nb for nb in possible_neighbors if (ld.x - nb.x)**2 + (ld.y - nb.y)**2 < 0.5**2 ]
        for nb in neighbors:
            if (ld.target !=0) or (nb in visit):
                if nb not in visit:
                    ld.target-=1
                    visited['ldr'+str(ld.id)].append(nb)
                if ld.party==nb.party[0:3]:
                    mat[nb.id][party_code[ld.party]]+=uniform(0.0,0.5)
                else:
                    inc=uniform(-0.5,0.5)
                    mat[nb.id][party_code[ld.party]]+=inc
                    if inc>0:
                        mat[nb.id][party_code[nb.party[0:3]]]-=inc
            position_update(nb,0.3)
            
    if count%28 == 0:
        ldr=choice(ldrs)
        position_update(ldr)
                    
            
        
        
def draw_bar(ax0):
    x=['BJP','JDU','RJD','CON','LJP','OPT']
    x1=['Party1','Party2','Party3','Party4','Party5','Others']
    if count==1:
        y=[bjp,jdu,rjd,cong,ljp,op]
        global p1
        ax0.bar(x1,y,color=color[1:])
        plt.xlabel("Parties")
        plt.ylabel("Ratio")

    elif count == total_count:
        y1=[bjp,jdu,rjd,cong,ljp,op]
        y2=[]
        for val in x:
            cnt=0
            for ag in agents:
                if ag.party[0:3]== val:
                    cnt+=1
            y2.append(cnt/n)
        
        print('Initial=',y1)
        print('Final',y2)
        x_axis = np.arange(len(x))
        plt.setp(ax1, xticks=x_axis, xticklabels=x1)
        ax1.bar(x_axis - 0.2, y1, 0.4, label = 'Initial')
        ax1.bar(x_axis + 0.2, y2, 0.4, label = 'Final')
        #plt.xticks(x_axis, x)
        ax1.legend()
        plt.show()
        
    
                    
            

            
def boundary_check(ag):
    if ag.x<0:
        ag.x+=1
        if ag.y<0:
            ag.y+=1
        elif ag.y>10:
            ag.y-=1
    elif ag.x>10:
        ag.x-=1
        if ag.y<0:
            ag.y+=1
        elif ag.y>10:
            ag.y-=1
    if ag.y<0:
        ag.y+=1
        if ag.x<0:
            ag.x+=1
        elif ag.x>10:
            ag.x-=1
    elif ag.y>10:
        ag.y-=1
        if ag.x<0:
            ag.x+=1
        elif ag.x>10:
            ag.x-=1
                       
            
def movement():
    for ld in ldrs:
        position_update(ld,0.2)
    
                
def update_party():
    counter=0
    for i in mat:
        val=max(i)
        ind=i.index(val) 
        curr_pty=party_name[ind]
        typ=''
        if val>=8:
            typ='_core'
        elif val>=5 and val<8:
            typ='_med'
        elif val>=3 and val <5:
            typ='_low'
        agents[counter].party=curr_pty+typ
        counter+=1
        
                    
def rally():
    participants=[ag for ag in agents if ag.rally=='yes']
    for agt in participants:
        lead=choice(ldrs)
        if agt.party[0:3]==lead.party:
            mat[agt.id][party_code[lead.party]]+=uniform(-0.3,1.0)
        else:
            inc=uniform(-1.0,1.0)
            mat[agt.id][party_code[lead.party]]+=inc
            if inc>0:
                mat[agt.id][party_code[agt.party[0:3]]]-=inc
                
def tv_campaign():
    tv_holders=[ag for ag in agents if ag.tv=='yes']
    for leader in ldrs:
        for owner in tv_holders:
            if owner.party[0:3]==leader.party:
                mat[owner.id][party_code[leader.party]]+=uniform(0.0,0.3)
            else:    
                inc=uniform(-0.3,0.3)
                mat[owner.id][party_code[leader.party]]+=inc
                if inc>0:
                    mat[owner.id][party_code[owner.party[0:3]]]-=inc
            
                
def message():
    rec=[ag for ag in agents if ag.phone=='simple']
    for lds in ldrs:
        
        target=target_phone[lds.id]
        selected=sam(rec,target)
        '''for i in range(target):
            selected.append(choice(rec))'''
        for each in selected:
            if each.party[0:3]==lds.party:
                mat[each.id][party_code[lds.party]]+=uniform(0.0,0.25)
            else:    
                inc=uniform(-0.2,0.25)
                mat[each.id][party_code[lds.party]]+=inc
                if inc>0:
                    mat[each.id][party_code[each.party[0:3]]]-=inc
            
            
    
            
            
            
         

                    



def update():

    global agents
    global count
    count+=1
    door_interaction()
    '''if count%rally_count ==0:
        rally()
    if count%(total_count/28) == 0:
        tv_campaign()
    if count%152 == 0:
        message()'''
    update_party()
    
    if count<total_count+1:
        movement()
    
    if count==total_count:
        print(perct('party','BJP_med')) 
        print(perct('caste','OBC')) 
        print(perct('tv','yes')) 
        print(supp_dist['BJP_med'])
        for ld in ldrs:
            print(ld.target)
    draw_bar(ax0)
    
    
    
    
        
    
        
    
    
    
            
import pycxsimulator
pycxsimulator.GUI().start(func=[initialize,observe, update])