#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 18:12:22 2018

@author: eguchimasato

*Use else to chatch error.

import time help to count down
I can do \t\t to space cosistant

DocString:
    Introduction: This game aims to learn Japanese through shopping. User are expected memorize
    Japanese words and type them. The less mistakes you make, the higher you score is.(allowance)
    You have 3 rounds of shopping. You will not notified what to buy until you go to store.　When
    your budges run out, the game is over. You can choose to keep playing at the end of the game.
    
    bugs: You can scroll up to cheat. Don't cheat!
        
"""

from sys import exit

your_money = 5000
money_for_shopping = 2500

#fruits_list = ["budou","momo","ringo"]
#vegetables_kist = ["hourenso","jagaimo","nasu","ninjin"]
#fish_list = ["ika","kai","maguro","shake","tako"]

fruits_dic = {"momo":"peach","budou":"grape","ringo":"apple"}
vegetables_dic = {"hourenso":"spinach","jagaimo":"potato","nasu":"egg plant","ninjin":"carrot"}
fish_dic = {"ika":"squid","kai":"shell fish","maguro":"tuna","shake":"salmo","tako":"octopus"}

price_list = {"momo":200,"budou":300,"ringo":150,"hourenso":450,"ninjin":300,"jagaimo":500, "nasu":350,"ika":300,"kai":350,"maguro":700,"shake":500,"tako":400, "go back":500}

stage1_needed_items = ["budou"]
stage2_needed_items = ["hourenso", "npoasu"]
stage3_needed_items = ["ika", "maguro", "tako"]

memo_1 = """Here is the list of the items you may buy today
              English         Japanese\n
              peach-----------momo\n
              grape-----------budou\n
              apple-----------ringo"""
            
memo_2 = """Here is the list of the items you may buy today\n
             English        Japanese\n
             spinach--------hourenso\n
             potato---------jagaimo\n
             egg plant------nasu"""

memo_3 = """Here is the list of the items you may buy today\n 
              English         Japanese\n
              squid-----------ika\n
              shell fish------kai\n
              tuna------------maguro\n
              salmon----------shake\n
              octopus---------tako"""

bought_items = []

def game_starter():
    print("""     You have a party and have to go shopping with Masato. But he doesn't know much
     English so you have to tell him what to buy in Japanese. Your mom gave you ¥5000 and you 
     need ¥2500 to compelete your shopping. The left over will be your allowance so try not to buy 
     unnecessary items. If you forget Japanese words, you can always look memo but it costs ¥500. 
     Can you successfully complete shopping with Masato? """)
    
    input("Press enter to start game")
    
    
def money_indicator():
    """show remaind cash"""
    print(f"""                                                 You have ¥{your_money} remaining""")
    print(f"""                                                 You need ¥{money_for_shopping} to complete all of your shopping""")


def money_substractor_right_item(item):
    """substract money from your wallet when you buy a right item"""
    global your_money
    your_money = your_money - price_list[item]
    global money_for_shopping
    money_for_shopping -= price_list[item]
    
    
def money_substractor_wrong_item(item):
    """substract money from your wallet when you buy a wrong item"""
    global your_money
    your_money -= price_list[item]

    
def shopping1():
    """keep telling Masato what to buy until conpleate all the shopping"""
    
    bought_items = []
    print("FIRST STAGE:FRUITS")
    print(memo_1)
    input("Press enter when you are ready (list will be gone)")
    page_cleaner()
   
    while stage1_needed_items != bought_items:
        
        global your_money
        global money_for_shopping

        if  your_money >= money_for_shopping:            
            money_indicator()
            print("To check the list again,type 'go back' (costs ¥500))")
            print(f"""We need a {fruits_dic[stage1_needed_items[0]]}.""")
            print(f"""Your bascket:{bought_items}""")
            your_order = input("Tell Masato 1 item to buy in japanese >").lower()
            print("\f")
        
            if your_order in bought_items:
                print(f"We've already bought this item. So Masato just ate it. It cost ¥{price_list[your_order]}.")
                money_substractor_wrong_item(your_order)
            
            elif your_order in fruits_dic and your_order not in stage1_needed_items:
                
                print(f"""Masato returned with a {fruits_dic[your_order]}. We don't need it! but Masato just ate it.It cost ¥{price_list[your_order]}.""")
                money_substractor_wrong_item(your_order)
                
            elif your_order in fruits_dic:
                print(f"""Masato returned with a {fruits_dic[your_order]}. Yes, that's what we want! It cost ¥{price_list[your_order]}.""")
                bought_items.append(your_order)
                bought_items.sort()
                money_substractor_right_item(your_order)
                
            elif your_order == "go back":
                print(memo_1)
                money_substractor_wrong_item(your_order)
                input("Press enter when you are ready (list will be gone)")
                page_cleaner()
                
            elif your_order not in fruits_dic:
                print("Masato doesn't know the word!")
                
            else:
                print("Please try again, something went wrong")
            
        elif your_money < money_for_shopping:
            fail()
            
        else:
            print("This program has an error")
    
    stage_clear()
            
def shopping2():
    """keep telling Masato what to buy until conpleate all the shopping"""
    bought_items = []
    print("SECOND STAGE:VEGETABLES")
    print(memo_2)
    input("Press enter when you are ready (list will be gone)")
    page_cleaner()

    while stage2_needed_items != bought_items:
        
        global your_money
        global money_for_shopping

        if  your_money >= money_for_shopping:            
            #print(f"""These are what you wann to buy today! grape and peach""")
            money_indicator()
            print("To check the list again,type 'go back' (costs ¥500))")
            print(f"""We need {vegetables_dic[stage2_needed_items[0]]} and {vegetables_dic[stage2_needed_items[1]]}.""")
            print(f"""Your bascket:{bought_items}""")
            your_order = input("Tell Masato 1 item to buy in japanese >").lower()
            print("\f")
    
            if your_order in bought_items:
                print(f"We've already bought this item. So Masato just ate it. It cost ¥{price_list[your_order]}.")
                money_substractor_wrong_item(your_order)
            
            elif your_order in vegetables_dic and your_order not in stage2_needed_items:
                
                print(f"""Masato returned with a {vegetables_dic[your_order]}. We don't need it! but Masato just ate it.It cost ¥{price_list[your_order]}.""")
                money_substractor_wrong_item(your_order)
                
            elif your_order in vegetables_dic:
                print(f"""Masato returned with a {vegetables_dic[your_order]}. Yes, that's what we want! It cost ¥{price_list[your_order]}.""")
                bought_items.append(your_order)
                bought_items.sort()
                money_substractor_right_item(your_order)
                
            elif your_order == "go back":
                print(memo_2)
                money_substractor_wrong_item(your_order)
                input("Press enter when you are ready (list will be gone)")
                page_cleaner()
                
            elif your_order not in vegetables_dic:
                print("Masato doesn't know the word!")
                
            else:
                print("Please try again, something went wrong")
            
        elif your_money < money_for_shopping:
            fail()
            
        else:
            print("This program has an error")
            
    stage_clear()
            
def shopping3():
    """keep telling Masato what to buy until conpleate all the shopping"""
    bought_items = []
    print("THIRD STAGE: FISH")
    print(memo_3)
    input("Press enter when you are ready (list will be gone)")
    page_cleaner()

    while stage3_needed_items != bought_items:
        
        global your_money
        global money_for_shopping

        if  your_money >= money_for_shopping:            
            money_indicator()
            print("To check the list again,type 'go back' (costs ¥500))")
            print(f"""We need {fish_dic[stage3_needed_items[0]]}, {fish_dic[stage3_needed_items[1]]} and {fish_dic[stage3_needed_items[2]]}.""")
            print(f"""Your bascket:{bought_items}""")
            your_order = input("Tell Masato 1 item to buy in japanese >").lower()
            print("\f")
        
            if your_order in bought_items:
                print(f"We've already bought this item. So Masato just ate it. It cost ¥{price_list[your_order]}.")
                money_substractor_wrong_item(your_order)
            
            elif your_order in fish_dic and your_order not in stage3_needed_items:
                
                print(f"""Masato returned with a {fish_dic[your_order]}. We don't need it! but Masato just ate it.It cost ¥{price_list[your_order]}.""")
                #bought_items_by_mistake.append(your_order)
                money_substractor_wrong_item(your_order)
                #print(bought_items_by_mistake)
                
            elif your_order in fish_dic:
                print(f"""Masato returned with a {fish_dic[your_order]}. Yes, that's what we want! It cost ¥{price_list[your_order]}.""")
                bought_items.append(your_order)
                bought_items.sort()
                money_substractor_right_item(your_order)
                
            elif your_order == "go back":
                print(memo_3)
                money_substractor_wrong_item(your_order)
        
                input("Press enter when you are ready (list will be gone)")
                page_cleaner()
            elif your_order not in fish_dic:
                print("Masato doesn't know the word!")
                
            else:
                print("Please try again, something went wrong")
            
        elif your_money < money_for_shopping:
            fail()
            
        else:
            print("This program has an error")
            
def stage_clear():
    print("Congraturations. You Cleared this stage!!")
    input("Press enter to go to next stage >")
    
def fail(): # rename as fail
    print("You don't have enough money to complete the shopping!")
    print("Game_over!!")
    restarter()
    
def grade_viewer():
    allowance = your_money - money_for_shopping
    print("Congraturations! You've completed all the shoppings!")
    print(f"""You got ￥{allowance} as your allowance.""")
    
def restarter():
    global your_money
    global money_for_shopping
    desicion = input("Do you want to play again? Y/N >").upper()
    
    if desicion == "Y":
        your_money = 5000
        money_for_shopping = 2500
        shoppings()
        
    elif desicion == "N":
        print("Thank you for playing")
        exit(0)
    
    else:
        print("Please enter Y or N >")
        restarter()
        
def page_cleaner():
    print("\n"*50)

def shoppings():
    shopping1()
    shopping2()
    shopping3()
    grade_viewer()
    restarter()

#**********************
game_starter()
shoppings()
#***********************


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

