from typing import Callable, Any, Optional

from .activities import OwnedActivities, Jobs, Outlets
from . import activities
from . import layout
from . import format


class StepBuilder:
    def __init__(self, default_output: Optional[str] = None, default_content: Optional[str] = None):
        self.default_output = default_output
        self.default_content = default_content
        self.output = default_output
        self.content = default_content
        self.section = None
        
    def outln(self, line=''):
        if self.output is None:
            self.output = line.strip('\n')
        else:
            self.output += '\n' + line
            
    def mainln(self, line=''):
        if self.content is None:
            self.content = line.strip('\n')
        else:
            self.content += '\n' + line
            
    def reset(self):
        self.section = None
        self.output = self.default_output
        self.content = self.default_content
        

def generate(add_step: Callable[[str, str, str], Any], status_line, example_job: OwnedActivities):
    sb = StepBuilder()
    def add():
        add_step(sb.output, sb.content, sb.section)
        sb.reset()

    goal_activity = activities.from_id(activities.Stage1GoalActivityId)
    
    sb.outln("- hi! welcome to the tutorial! glub. i'm deka! one of the devs on this")
    sb.outln("- Hey, what's up? I'm Triska, and I'm kind of the 8est.")
    sb.outln("- she also rly likes 8. and spiders. seriously she is going to use 8 for both 'B' and 'ate' sounds. im sorry in advance")
    sb.outln("- Pfffffffft whatever. You keep typing 'glub' and have that weird smilie with the '3' hat.")
    sb.outln("- blasphemy 38O glub is good. anyways we're here to show you how to play this game!")
    add()

    sb.outln("- This game is an idle clicker where you try to earn money to fund a 8uncha cre8tive stuff.")
    sb.outln("- yeah, and it's themed around the creative process")
    add()
    
    sb.outln("- It's also designed to be played from the command line, which explains why it looks so 8ad!")
    sb.outln("- sorry about that, glub 38(")
    sb.outln("- Aw, 8ut Luckily for you, we've put together this little GUI version so you can more easily test it.")
    add()
    
    sb.outln("- (ty btw for that, your feedback is v much appreciated glub)")
    sb.outln("- Mmmmmmmm, yeah, I guess this game wouldn't happen without your tireless efforts, 8eta tester. So we should thank you for that.")
    add()
    
    sb.outln("- anyways! on to the actual game, glub!")
    add()

    sb.outln("- Yeah, what's the goal here?")
    sb.outln("- 'click' on stuff! glub. well using the menu. and see how quick you can get to the ultimate goal!")
    sb.outln("- Ultim8 goal? And what is that exactly?")
    sb.outln("- to try and buy the biggest most important thing! the ability to create a construct, glub")
    sb.outln("- That's... 8izarre. And what does that even mean?")
    add()

    sb.outln("- it means you're trying to buy {:s}. and its only weird bc we dont have the next phase in the game yet!".format(goal_activity.name))
    sb.outln("- Yeah, gotta make sure we get phase 1 all good with testers 8efore moving on to the next. Pretty sure it'll 8e weird after that too, though.")
    sb.outln("- oh well get over it")
    sb.outln("- Already past it. Let's move on to how to actually play.")
    sb.outln("- glub!")
    
    sb.mainln(status_line)
    sb.default_content = status_line
    sb.section = "1.) Status Line"
    sb.outln("- Okay, so this thing is the main status line.")
    sb.outln("- mmm, glub? the what now? which part?")
    add()
    
    sb.mainln("\________________  _______________/")
    sb.mainln("                 \/")
    sb.mainln("          THIS THING, 8ITCH")
    sb.outln("- That thing.")
    sb.outln("- wow rude.")
    sb.outln("- Hey, 8ut at least you know what I'm talking a8out ::::P")
    add()
    
    sb.outln("- okay, glub, but what does each part mean?!")
    sb.outln("- Oh my gog, calm down, I was getting to that! Now, check this...")
    add()
    
    sb.section = "1.1.) -- Money"
    sb.mainln('\/')
    sb.outln("- This first num8er here, that's how much money you got.")
    sb.outln("- it says 0 glub")
    sb.outln("- Well, yeah it says 0! You think you get to start off with money? May8e in happy fantasy human land, sure. 8ut this 8nt that, chief. You start with $0.")
    sb.outln("- okay miss im-so-smart-spider, how do we get more money then???")
    add()
    
    sb.outln("- You gotta click an activity! Jobs usually make the most money, 8ut outlets can get you some change too, sometimes.")
    sb.outln("- makes sense, glub. With the click button that's usually there.")
    sb.outln("- Yeah, having that show up IN this tutorial would have 8een a little too complic8ed.")
    add()
    
    sb.section = "1.2.) -- Creative Juice"
    sb.mainln("   \___________/")
    sb.outln("- okay! i got the next one! so, this here is how much juice you have.")
    sb.outln("- Hahahahahahahaha, juice, huh? Sounds lewd.")
    sb.outln("- omg its not lewd!!! >.< CREATIVE juice!")
    sb.outln("- Sure, whatever you say ::::) So what does it do?")
    add()
    
    sb.outln("- oh, it mostly powers Outlets! when you do an outlet, you gotta have enough creative juice to start it! and that juice is used as long as the Outlet is running. but dont worry! you'll get it back when the Outlet is done running. The first number is how much you have free, and the 2nd number is how much total you have!")
    sb.outln("- ...")
    sb.outln("- hey you okay?")
    sb.outln("- Oh, yeah. Sorry, can't expect me to keep my eyes open during that 8oring, 8oring, 8ORING speech.")
    sb.outln("- um. glub 38/ im not really sure how to make this more interesting?")
    add()
    
    sb.outln("- Easy, I got this. Check it.")
    add()
    
    sb.section = "1.3.) -- Seeds & (i)deas"
    sb.mainln("                   \_____/")
    sb.outln("- So this one is pretty complic8ed, 8ut don't worry, you got *me* telling you a8out it ::::) Just the kind of friend that I am.")
    sb.outln("- shes SUCH a good friend that she brags about it instead of actually explaining 383")
    sb.outln("- Quiet, you! Anyways, this part is your Seeds and (i)deas... ...pfft")
    sb.outln("- what?")
    sb.outln("- Heheheheheheheheh. Seed XXXXD")
    add()
    
    sb.outln("- ...oh my fucking god could you stop making everyfin dirty for 2 seconds")
    sb.outln("- Look, I'm just saying the names. You decided on them, not me ::::) ...8wahahahahaha, seeds.")
    sb.outln("- ARE YOU GONNA EXPLAIN IT OR JUST KEEPING MAKING DIRTY JOKES GLUB?!")
    sb.outln("- Okay, okay, Fine, jeez.")
    add()
    
    sb.outln("So, Seeds are built up over time 8y progressing. Once you have at least one, you can medit8 to turn them into (i)deas.")
    sb.outln("- okay imma meditate all the time then! glub!")
    sb.outln("- What, no? That's gonna 8reak everyth8ng, you dum8ass glu8!!!!!!!!")
    sb.outln("- ... 38(")
    sb.outln("- What?")
    add()
    
    sb.outln("- im not a dumbass glub, glub 38'((")
    sb.outln("- W8, seriously?")
    sb.outln("- yes seriously that was rly mean im not doing this anymore. im turning off the display! GLUB!")
    sb.outln("- Deka, you can't just-")
    add()
    
    sb.default_content = ''
    sb.content = ''
    sb.outln("Oh my gog, she actually did it.")
    add()
    
    sb.outln("- Hmmph >38T")
    sb.outln("- Are you really going to 8e like this?")
    sb.outln("- idk are you really going to keep being a '8itch'?")
    add()

    sb.outln("- *sigh* Look, I'm SORRY, okay?")
    sb.outln("- you mean it?")
    sb.outln("- Sure, whatever. Now may8e give the screen 8ack?")
    sb.outln("- nuh-uh. not until you SOUND like you mean it")
    add()

    sb.outln("- ... Okay. Fine. Deka, I'm sorry. I respect you and your glu88ing, and I was rude. I won't do it again.")
    sb.outln("- okay.")
    sb.outln("- Okay?")
    sb.outln("- yes. thank you. here.")
    add()
    
    sb.default_content = status_line
    sb.content = status_line
    sb.outln("- Thank fuck. Okay, sorry a8out that little interruption, now 8ack to 8usiness.")
    sb.outln("- yay! now, why wouldn't i want to spend all the time meditating?")
    sb.outln("- Right, so that will reset the entire game. Except for (i)deas you already have, of course. Oh and Autom8ions. You keep those too.")
    sb.outln("- oooooooooh i get it, so it's like the prestige of this thing!")
    sb.outln("- Exactly!")
    add()
    
    sb.outln("- but what do you even DO with (i)deas glub?")
    sb.outln("- Good question! Right now they're pretty much only used for buying automations.")
    sb.outln("- 38?")
    sb.outln("- Automations let your activities run without clicking.")
    sb.outln("- wait you mean i gotta prestige before i can even make the idler be idle?")
    add()
    
    sb.outln("- Well, yeah. 8ut it shouldn't take too long to get your first seed. ppfpptptatfff")
    sb.outln("- 38T well anyways, that makes sense so far.")
    sb.outln("- Of course it did, after all, it was me who explained it to you ::::)")
    sb.outln("- i feel so special")
    sb.outln("- You should! Hey, wanna take the last part of the status line? To make up for that crap 8efore.")
    add()
    
    sb.section = "1.4.) -- Game Time"
    sb.mainln("                             \____/")
    sb.outln("- sure! it's p easy, the last one is just game time! it's the number of seconds since the game was started.")
    sb.outln("- Perfect! See, I told you you were a little 8adass :::;)")
    sb.outln("- glub! i dont remember you saying that but ill take the compliment 38D")
    add()
    
    sb.outln("- And that's it for the status line!")
    sb.outln("- ooh, what's next?")
    sb.outln("- How a8out the activity card?")
    sb.outln("- Yeah, let's do it!")
    add()
    
    # +------------------------------------------------+--------------+
    # | Eat Bagels                          ($20) x1:0 |    (No auto) |
    # | $0 (0.00J)                      $1/C 0.0000J/C |        x{:d} |
    # | |                                 | 999h60m55s |      RUNNING |
    # +------------------------------------------------+--------------+
    act_card = layout.bar() + '\n' + layout.make_act_card(example_job, 0.0) + '\n' + layout.bar()
    sb.default_content = act_card
    sb.content = act_card
    sb.section = "2.) Activities"
    sb.outln("- this is an activity, glub. you see these on the main screen!")
    add()
    
    sb.outln("- Easy, this is a clicker, right? So those have gotta 8e the things you click on.")
    sb.outln("- yeah, you're exactly right!")
    sb.outln("- Am I ever wrong? ::::)")
    sb.outln("- p frequently but not this time! glub 38D")
    add()
    
    sb.outln("- okay, now every activity is either a 'job' or an 'outlet'. this one is a job, but outlets and jobs all look p much the same as this one!")
    sb.outln("- W8. If they all look the same, then it's really dum8 to have different kinds of activities.")
    sb.outln("- theres a difference tho! jobs will almost always get you more money, but outlets are better for getting more juice. oh and also outlets usually require a lotta juice to go.")
    add()

    sb.outln("- But some jo8s cost juice too! It's waaaaaaaay ar8itrary.")
    sb.outln("- ofc its arbitrary its a game 383")
    sb.outln("- Fair, I guess. For now. Still seems really, really dum8 to me 8ut I can roll with it.")
    add()

    draw = format.Draw(act_card, mutate=False)
    draw.corner_char = draw.horz_char = draw.vert_char = '*'

    sb.section = '2.1.) -- Name'
    sb.content = draw.rect((0, 0), (13, 2))
    sb.outln("- this is the name of the activity!")
    sb.outln("- I can see what a name is, my thinkpan 8n't 8roken, you know.")
    sb.outln("- sshhhhhhh its for a complete tutorial omg! glubglub!")
    sb.outln("- Fine, fine. 8ut does it mean anything special?")
    sb.outln("- mmmm, not rly. its just a fun way to categorize the different levels of activities.")
    sb.outln("- Got it.")
    add()

    sb.outln("- this one is called {!r}, it's a v important job!".format(example_job.name))
    sb.outln("- Why is that one so important? I dunno, Deka, this job seems like it needs to 8e taken down a notch.")
    sb.outln("- it's the first one you get! and it doesn't cost anyfin to run, ever!")
    sb.outln("- Ohhhhhhhh, so you can always run that one.")
    sb.outln("- yesh! 38)")
    sb.outln("- I guess it deserves it, then. All right, I'll allow it. I'm nice like that.")
    add()
    
    sb.section = '2.2.) -- Instances'
    sb.outln("- glubglub! next thing up! activity instances!")
    sb.outln("- This one is pretty weird, 8etter let me handle it.")
    sb.outln("- sure, go for it!")
    add()
    
    sb.outln("- So, you've got these different kinds of activities, right? 8ut you can get way, way more than just one copy of each.")
    sb.outln("- glub, and each copy is an in-")
    sb.outln("- Excuse me, I'm talking?")
    sb.outln("- okay ur right that one was on me im sorry.")
    sb.outln("- Thank you. Like I was saying, each copy is called an 'instance'.")
    add()
    
    sb.outln("- i will be v honest, 'instance' sounds rly rly technical so i might call them 'copies' in this tutorial.")
    sb.outln("- A8solutely! 'instance' is a pretty complic8ed word for you, so you go right ahead and use wrong ones if you would like ::::)")
    sb.outln("- ...well that wasnt a v nice way of saying it but its fine glub 38/")
    sb.outln("- Gr8! Moving on...")
    add()
    
    sb.content = draw.rect((37, 0), (50, 2))
    sb.outln("- This part on the activity is where you can see inform8ion on its instances.")
    sb.outln("- that first part looks like a dollar amount to me and not number of copies glub.")
    sb.outln("- The number in parenthesis? Well, yeah, it's not a number of 'copies' or even a number of instances")
    sb.outln("- bluh 38P what is it then?")
    add()

    sb.outln("- That's the price of the next instance of that activity.")
    sb.outln("- ooh, so you can buy them from here?")
    sb.outln("- Nope, just a reminder! It's the same price that's listed in the Store.")
    sb.outln("- okay, nice!")
    add()
    
    sb.outln("- Hell yeah, it's nice!!!!!!!! It's pretty much the most convenient thing I can think of. Good thing I came up with it while testing.")
    sb.outln("- normally id say debatable but you v much earned that one. ty.")
    sb.outln("- You're welcome! See, that wasn't so hard, I do something nice and you say 'thanks'. And then every8ody feels all nice inside.")
    sb.outln("- sure! ill keep thanking you every time you actually do something >38)")
    sb.outln("- That's so magnimonious of you!")
    add()
    
    sb.outln("- 'magnimonious'? idk Triska that's a p big word for you. u shore u know what it means?")
    sb.outln("- Yup! The opposite of what you are 8eing.")
    sb.outln("- actually im p sure that is true. yay!")
    add()
    
    sb.outln("- 8ack to 8usiness! So the '1x' after that price tells how many active instances you have.")
    sb.outln("- glub! *raises hand*")
    sb.outln("- Yes? The catdogmermaid clown in the front row?")
    sb.outln("- ooh, just, 'active' instances? does that mean you can have some copies be inactive?")
    sb.outln("- That's right. When you buy new instances they're set to active 8y default as long as you have the resources for it.")
    add()
    
    sb.outln("- when could you ever NOT have the resources?")
    sb.outln("- That can happen if you're running an activity already and you try to buy more instances to boost the rewards before it finishes. If you don't have enough juice and money to support starting the new instance, you'll still buy the new instance but it won't be set to active.")
    sb.outln("- woah, ill have to be careful not to do that glub!")
    add()

    sb.outln("- It isn't really a 8ig deal when it happens, you just won't 8e a8le to set them active until either the current run finishes or you get the resources.")
    sb.outln("- okay thats not so bad then")
    add()
    
    sb.outln("- It's not, 8ut it also means you don't get the extra reward.")
    sb.outln("- glub 38x")
    sb.outln("- I don't know what that means 8ut okay. Now, you can also set the number of active instances lower or higher yourself if you want.")
    add()

    sb.outln("- why would you do that?")
    sb.outln("- I told you, it lowers the cost of runs! Weren't you listening????????")
    sb.outln("- you said it applied to after you bought new ones, when you already had the activity running. i wanted to be sure glub")
    sb.outln("- Okay, fair. 8ut yeah, your instinct is dead-on - deactivating instances DOES lower the resource cost 8ut it also lowers the reward. So use it wisely!")
    sb.outln('- i shall do my glubbin best')
    add()

    sb.outln("- Good. If you do end up setting some instances inactive, the number of inactive copies is shown after the colon.")
    sb.outln("- ah, where it says ':0' in the example, right?")
    sb.outln("- Yeah. There aren't ANY inactive instances in this example, so that's why it's 0.")
    add()

    sb.section = "2.3.) -- Costs"
    sb.outln("- Okay, I'm tagging out. You're up, Deka.")
    sb.outln("- glub! up next, activity costs!")
    add()
    
    sb.content = draw.rect((0, 1), (13, 3))
    sb.outln("- this part is how much it costs to start this activity, to 'click' it!")
    sb.outln("- To 'click' it? I thought this was a text-8ased idler.")
    sb.outln("- yeahhh thats why the ui is so bad. it's a click though. or 'execution'. or 'run'.")
    sb.outln("- That is way too many words for the same thing!!!!!!!!")
    sb.outln("- deal w it 3B)")
    add()
    
    sb.outln("- glub! the first number is how many dollars it costs to start, and the second one is how much juice it will take up while running.")
    sb.outln("- Why exactly does it cost dollars to start something that *makes* dollars? Sounds like 8ad game design to me!")
    sb.outln("- no! bc, sometimes there are some activities that gotta 8e limited! or things would get v v v *v* unbalanced later on!")
    add()

    sb.outln("- If you say so.")
    sb.outln("- i do! glub!")
    add()

    sb.outln("- you dont get those dollars back, either. but you DO get the juice back.")
    sb.outln("- But if it's a jo8 you DO get the dollars 8ack, kind of. Don't jo8s always give more money than they take to start?")
    sb.outln("- yeah that's right!")
    add()
    
    sb.outln("- one more thing! the costs that you see are updated for the number of active copies of that activity. if you update them, the cost changes")
    sb.outln("- That... makes a surprising amount of sense.")
    sb.outln("- i do that sometimes 38>")
    add()
    
    sb.section = '2.4.) -- Production'
    sb.outln("- Ooh, this next part is gr8. Making money!")
    sb.outln("- none of it is reel glub but okay")
    sb.outln("- Doesn't matter, I'm still going to have the most. 8ecause, as we all know, I'm the 8est.")
    sb.outln("- thats only gonna happen if you can tell what is going on with production !!")
    add()
    
    sb.content = draw.rect((33, 1), (50, 3))
    sb.outln("- You mean this thing? It's super simp, I'll 8e okay.")
    sb.outln("- well you shore arent gonna 'make money' w this one! it's only gonna give you $1")
    sb.outln("- Yeah, and no juice at all. 8ut that's 8ecause of all the example activities, you chose the one that's the worst!!!!!!!!")
    sb.outln("- tutorials should be simple glub")
    sb.outln("- Only if you're too simple minded for the good shit :::;)")
    add()
    
    sb.outln("- okay well its what we got so deal w it")
    sb.outln("- It's fiiiiiiiine I can take it.")
    sb.outln("- so take it already. answer some questions! glub! like, how do you get more juice?")
    add()
    
    sb.outln("- All right, all right. So we've said it to death already 8ut in case you, dear reader, are skipping the start and jumping str8 to act 5...")
    sb.outln("- this is a tutorial there are no acts. wtf are you glubbin on about???")
    sb.outln("- Fine, section, what is this, 2.4? Yeah. Well, in case you did skip here, there's 8oth jobs and outlets.")
    sb.outln("- mmhmm! and this one is a job!")
    add()
    
    sb.outln("- Which means, it'll 8e a lot 8etter at getting you money 8ack, 8ut it isn't super heavy on the juice.")
    sb.outln("- and do outlets do the opposite?")
    add()
    
    example_outlet = OwnedActivities(Outlets[0], 1, 1, 0, False)
    outlet_card = layout.make_act_card(example_outlet, 0.0)
    sb.content = draw.overtype_lines((0, 1), outlet_card.split('\n'))
    sb.outln("- Yes! Like this one, {!r}. They give permanent increases to juice.".format(example_outlet.name))
    sb.outln("- woah it costs a buncha money though")
    sb.outln("- That's the price you pay to 8e 8adass. Just, get money from the jo8s and it'll 8e fine.")
    sb.outln("- that is true")
    add()
    
    sb.outln("- ooh, back to this job!")
    sb.outln("- Wow, your love for 8agels is cringe.")
    sb.outln("- its not cringe its cool! glub >38T")
    sb.outln("- You know what? Valid. F8ck the world and what they think.")
    sb.outln("- yeah! glub!")
    add()

    sb.section = "2.5.) -- Duration"
    sb.outln("- glub! next up, activity duration!")
    sb.outln("- Dur8ion... so that's how long something takes.")
    sb.outln("- right")
    add()
    
    sb.content = draw.rect((0, 2), (36, 4))
    sb.outln("- here is the activity progress bar")
    sb.outln("- 8ar? That is an 'X'.")
    sb.outln("- yeah, thats cause it's not running yet glub")
    sb.outln("- Soooooooo, not really a 8ar then.")
    add()
    
    sb.outln("- not *now*, but once we give it a click...")
    add()

    # quick make fake act
    running_job = example_job.copy()
    running_job.execute(0.0)
    running_card = layout.make_act_card(running_job, 0.3)
    sb.content = draw.overtype_lines((0, 1), running_card.split('\n'))
    sb.outln("- then the progress bar shows up! glub!")
    sb.outln("- Ayyyyyyyy there it is! Finally.")
    add()
    
    sb.outln("- and ofc, once it finishes...")
    add()
    
    sb.content = draw.overtype_lines((0, 1), running_card.split('\n'))
    sb.outln("- Ah, it goes 8ack to 8eing an 'X'.")
    sb.outln("- yep! 38)")
    add()
    
    sb.outln("- And there's a number to the right of the 8ar. Let me guess... countdown to compl8ion?")
    sb.outln("- got it the first time!")
    add()
    
    sb.outln("- when it's running, it'll countdown. when it's not running, it's just how long it will take once it starts.")
    sb.outln("- Easy. Pro8a8ly the most str8forward part of this entire game. Nice jo8.")
    sb.outln("- tyty")
    add()
    
    sb.section = '2.6.) -- Automations'
    sb.outln("- so i think that's it for activity cards, right?")
    sb.outln("- What? No, hold on! You missed something!!!!!!!!")
    sb.outln("- glub?")
    sb.outln("- Don't 'glu8' me! You skipped the entire right side, the autom8ions section!")
    sb.outln("- oh right the automations!")
    add()
    
    sb.content = draw.rect((50, 0), (64, 4))
    sb.outln("- Yeah, this whole entire side!")
    sb.outln("- that is a lot of activity card to miss im sorry glub")
    sb.outln("- Don't worry a8out it. I got your 8ack :::;)")
    sb.outln("- ty based co-host T_T")
    sb.outln("- Anytime.")
    add()
    
    sb.outln("- So the autom8ions are for making the activities run without you clicking on them.")
    sb.outln("- its the idle part of the idler! 38O")
    sb.outln("- Yeah, so pretty important stuff!")
    add()
    
    sb.outln("- You don't start out with any, 8ecause that would make the game way too easy.")
    sb.outln("- then, glub. how do you get some?")
    sb.outln("- We already covered this! It's-")
    add()
    
    sb.outln("- wait glub i remember! it's (i)deas, right? that you get from prestiging!")
    sb.outln("- From the medit8ion thing, yeah. Then you go to the store to exchange some of them for autom8ions.")
    add()
    
    sb.outln("- And once you finally 8uy one...")
    add()
    
    auto_job = example_job.copy()
    auto_job.automations += 1
    auto_job.automated = True
    auto_card = layout.make_act_card(auto_job, 0.0)
    sb.content = draw.overtype_lines((0, 1), auto_card.split('\n'))
    sb.default_content = sb.content
    sb.outln("- ...It'll look like this!")
    sb.outln("- ooh")
    add()
    
    sb.outln("- what is that number with the 'x' by it?")
    sb.outln("- Aha, I see you found the multiplier!")
    sb.outln("- multiplier?")
    sb.outln("- Yeah, see, the 8adass thing a8out automations is that if you get more than one, they start increasing your production.")
    sb.outln("- that's rly rly good!")
    add()
    
    sb.outln("- Hell yeah it is! And that multiplier number tells how much your production is getting 8umped up.")
    sb.outln("- but, you said the first one doesn't give you one?")
    sb.outln("- Nope! Well, if you want to get pedantic a8out it, I guess its multiplier is x1. 8ut who cares a8out that?")
    sb.outln("- i mean. glub. its good for consistency in the code and making a clean design and having the coupling of separate componen-")
    add()
    
    sb.outln("- Yeah, no8ody cares a8out any of that.")
    sb.outln("- i care glub >38(")
    sb.outln("- Okay, no8ody READING this cares.")
    sb.outln("- you may have a point there")
    sb.outln("- Yes!")
    add()
    
    sb.outln("- Anyways, the point is that even though the first autom8ion for an activity gives you nothing for a 8onus, every one you 8uy after that does.")
    sb.outln("- and its still good to automate even without a bonus")
    sb.outln("- True. It's money for free! And who wouldn't want that?")
    sb.outln("- fukin nobody thats who! glub!")
    sb.outln("- Yeah!")
    add()
    
    sb.outln("- Woah.")
    sb.outln("- what?")
    sb.outln("- That's it! We covered the entire activity card. It only took us like half a year.")
    sb.outln("- oh stop your glubbing. if the readers are bored they can just use the handy section jumpy thingy on the right.")
    sb.outln("- That is true. And hey, at least it was fun. So what's up next?")
    add()
    
    sb.default_content = None
    sb.content = ''
    sb.section = "3.) Store"
    sb.outln("- next we gotta talk about the store!")
    sb.outln("- All right, time to 8uy more instances and autom8ions.")
    sb.outln("- thats the place to do it 38)")
    add()
    
    example_jobdef = Jobs[0]
    sb.content = layout.bar() + '\n'
    sb.content += layout.make_act_store_listing(example_jobdef, 1, 0) + '\n'
    sb.content += layout.bar()
    sb.default_content = sb.content
    draw = format.Draw(text=sb.content, mutate=False)
    draw.corner_char = draw.vert_char = draw.horz_char = '*'
    sb.outln("- tada! its a store item")
    sb.outln("- A8solutely gorgeous. And confusing as shit. We're going over each part of this, right?")
    sb.outln("- ofc ofc! we wouldnt wanna leave the player in the dark")
    add()
    
    sb.section = '3.1.) -- Price'
    sb.content = draw.rect((0, 0), (17, 2))
    sb.outln("- first up, is this!")
    sb.outln("- The price tag.")
    add()
    
    sb.outln("- and the item name glub")
    sb.outln("- Yeah, I was thinking that may8e I didn't need to mention things that were super o8vious.")
    sb.outln("- its a tutorial idk if ppl jumped here or read everyfin or what")
    sb.outln("- If they're jumping around then it's on them!")
    sb.outln("- pls dun yell at the players for using the controls we gave them thats rude")
    add()
    
    sb.outln("- I'll do my 8est. No promises, though.")
    sb.outln("- good enough")
    add()
    
    sb.outln("- ooh, i just remembered something about price!")
    sb.outln("- What's that?")
    sb.outln("- oh its the amount of money it costs to buy something but thats not important right now")
    add()
    
    sb.outln("- ...Why ::::/")
    sb.outln("- yeshhhhhhh keep making that face i eat your dumb joke misery")
    sb.outln("- This is revenge isn't it? For all the juice jokes.")
    sb.outln("- maybe it is and maybe it isn't 38P")
    sb.outln("- Whatever. Anyways what were you gonna say?")
    add()
    
    sb.outln("- right! so price will go up with each copy of an activity that you buy")
    sb.outln("- What? Why?!")
    sb.outln("- to stop you from just buying infinity of the cheapest thing.")
    sb.outln("- Okay, that's fair. That would 8e a pretty 8oring game!")
    sb.outln("- exactly! i shore wouldnt wanna play if it were like that")
    add()
        
    # +---------------------------------------------------------------+
    # | $20 Eat Bagels                 - $0/C (0.00J)   | AUTO x1     |
    # | 1s                             + $1/C (0.0000J) | 1i          |
    # +---------------------------------------------------------------+
    
    sb.section = "3.2.) -- Duration"
    sb.outln("- So, not rel8ed, 8ut I have a question.")
    sb.outln("- what is it?")
    
    sb.content = draw.rect((0, 1), (5, 3))
    sb.outln("- Why is there a time listed here? Didn't we already see that in the activity cards?")
    sb.outln("- oh yeah! its just kind of a little reminder glub")
    add()
    
    sb.outln("- 8ut does it do anything?")
    sb.outln("- in the store? not really. its just a reminder 38)")
    add()
    
    sb.outln("- Okay, I guess it's good to know how long it takes 8efore 8uying it.")
    sb.outln("- exactly!")
    add()
    
    sb.section = "3.3.) -- Cost & Production"
    sb.content = draw.rect((31, 0), (50, 3))
    sb.outln("- glub! next up, the cost & production numbers!")
    sb.outln("- Ah, the part that tells what's going to happen after you 8uy another instance of this activity.")
    sb.outln("- yeah thats right! how bout you take this one?")
    add()
    
    sb.outln("- Hell yes, I'll take it!")
    sb.outln("- tyty glub")
    sb.outln("- So, there's two different lines there, one to show cost, and one to show production.")
    sb.outln("- 2 lines in one section! woah 38O")
    add()
    
    sb.content = draw.rect((31, 0), (50, 2))
    sb.outln("- Yeah, it's kind of a 8ig deal. The line starting with a '-' is what it costs to run an instance of the activity after you've 8ought it.")
    sb.outln("- ooh, like, on top of all the instances you already have?")
    sb.outln("- Yes! Look at that number, it's *waaaaaaaay* too small to be the whole thing.")
    sb.outln("- got it got it glub")
    add()
    
    sb.outln("- Okay, 8ut right now we're showing this stup8d eat 8agels task.")
    sb.outln("- why do you hate my bagels so much?")
    sb.outln("- Like, 1. It's kind of lame 8ut whatever. 8ut also, it doesn't ever cost anything to run!")
    sb.outln("- okay thats true. it's kind of boring.")
    sb.outln("- It's super 8oring! ::::( Let's take a look at something that *does* cost something.")
    add()
    
    example_cost_act = Jobs[1]
    next_task_card = layout.make_act_store_listing(example_cost_act, 1, 0) + '\n'
    sb.content = draw.overtype_lines((0, 1), next_task_card.split('\n'))
    mcost = format.money(example_cost_act.money_cost(1))[1:]  # no dollar sign
    s = "s" if example_cost_act.money_cost(1) != 1 else ""
    jcost = "{:.4f}".format(example_cost_act.juice_cost(1))
    
    sb.outln("- There we go.")
    sb.outln("- ooh, you're right, these numbers are much more interesting glub!")
    sb.outln("- Yes!")
    sb.outln("- so how does it work?")
    add()

    sb.content = draw.overtype_lines((0, 1), next_task_card.split('\n'))
    sb.outln("- Let's say you buy a new instance of this {:s} activity.".format(example_cost_act.name))
    sb.outln("- okay, shore! merbuyer deka buys one!")
    sb.outln("- Gr8, so starting a run of it would take {:s} dollar{:s} and {:s} juice, plus whatever it costs to run any copies you already have.".format(example_cost_act.name, mcost, s, jcost))
    sb.outln("- i think i get it! so its what gets added to the cost to run it.")
    sb.outln("- Yeah, exactly!")
    add()

    sb.outln("- So let's go 8ack to our 'friend', {:s}.".format(example_jobdef.name))
    sb.outln("- dont be rude to the bagels 38T")
    sb.outln("- Why? They don't care.")
    sb.outln("- bagels are yummy.")
    sb.outln("- They aren't, 8ut let's pretend they are. Whatever.")
    add()
    
    sb.content = draw.rect((31, 1), (50, 3))
    sb.outln("- See right here, this line starting with a '+'?")
    sb.outln("- glub! i see it as well as a pre-written scripted character in a tutorial can! 38D")
    sb.outln("- Good enough for me! So this is how much stuff you'll get from running the activity once you've bought another instance.")
    add()

    sb.content = draw.rect((31, 1), (50, 3))
    sb.outln("- oh so its the opposite of the cost")
    sb.outln("- Pretty much! It's kind of the 8est part of the store listing. All the loot you'll get from it!")
    sb.outln("- like buried treasure!")
    sb.outln("- Fuck yeah, exactly like 8uried treasure! 8ut 8uying it digs it up and gives it to you forever.")
    
    mprod = format.money(example_jobdef.money_rate(1))[1:]  # no dollar sign
    s = "s" if example_jobdef.money_rate(1) != 1 else ""
    sb.outln("- The thing is, {:s} is a p low-tier activity, so it only gives you {:s} dollar{:s}.".format(example_jobdef.name, mprod, s))
    sb.outln("- and no juice 38(")
    sb.outln("- Yeah, no juice ::::( 8ut if it did, that's where it would be.")
    add()
    
    sb.outln("- okay, and this extra juice and cash gets added to all other active instances, right?")
    sb.outln("- Yes! Now you're catching on. It's just like with cost.")
    sb.outln("- yay 38)")
    add()
    
    sb.section = "3.4.) -- Automation Price"
    sb.outln("- Next up for the store is the autom8ion section.")
    sb.outln("- ooh you're gonna tell us how to buy them finally??")
    sb.outln("- Hmmmmmmmm, nope! You are. This is 8oring so I'm tagging out, thanks ::::)")
    sb.outln("- i didnt actually agree to that but! i shall rise to the task! GLUB! >383")
    sb.outln("- Hell yes!!!!!!!! Take it away.")
    add()
    
    sb.content = draw.rect((50, 0), (64, 3))
    sb.outln("- glub! so this part here gives how much it costs to buy the next tier of automation!")
    sb.outln("- Oh right, and that num8er is gonna give how much it will multiply production 8y?")
    sb.outln("- it is. but it doesnt stack glub, bc its already pretty intense and rly good")
    sb.outln("- Yeah, it's pretty much the first thing that I'd go for. 8ecause it is the 8est.")
    add()
    
    sb.outln("- mmhmm. but they aren't cheap, glub.")
    sb.outln("- No shit! The price is in (i)deas, which if I'm remem8ering right, you can only get by medit8ing.")
    sb.outln("- yesssssssss!")
    add()
    
    sb.content = ''
    sb.default_content = ''
    sb.section = "4.) Good Luck"
    sb.outln("- Welp, looks like that's it.")
    sb.outln("- yeah that's all we got for you here!")
    sb.outln("- Seems pretty solid, click the things to get money and juice, get Seeds (pfft)...")
    sb.outln("- omg")
    sb.outln("- It's funny! Anyways, get Seeds, medit8 to turn them into (i)deas, use (i)deas to 8uy Autom8ions.")
    add()

    sb.outln("- oh and see how fast you can get to the ultimate goal! buying one instance of {:s}".format(goal_activity.name))
    sb.outln("- What happens after that?")
    sb.outln("- the end of phase 1! which is all thats in the game so far glub.")
    sb.outln("- So 8asically, getting there makes you a winner.")
    sb.outln("- yeah!")
    add()

    sb.outln("- Okay, cool.")
    sb.outln("- yes! and thats everything. you should give playing a shot!")
    sb.outln("- And if you can't figure something out, don't worry! We got your 8ack ::::)")
    sb.outln("- yush! you can send jello a DM on our main discord at dekarrin#0314, or you can open an issue on the GitHub page.")
    add()
    
    sb.outln("- i hope ur clicking goes well!")
    sb.outln("- Awwwwwwww yeah. Good luck out there. 8ye for now.")
    sb.outln("- bye-bye! glub 38D")
    add()
    
    sb.outln("(close this window to end the tutorial)")
    add()
