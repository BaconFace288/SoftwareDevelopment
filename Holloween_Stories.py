# Name, Age, Favorite Candy, Character traits, a fun fact, and the location of where the story takes place are required.
from openai import OpenAI
client = OpenAI(api_key="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")
def Story():
    Char_Name = input("Hello! Welcome to the holloween story maker. Input the name of your character: ")
    Char_Age = input("Now, input your character's age: ")
    Char_Fav_Candy = input("What is their favorite candy? Input it here: ")
    Char_Trait = input("Input a trait for your character: ")
    Char_FFact = input("Tell a fun fact about the character: ")
    Stor_Local = input("And finally, where does this story take place? ")
    check = input("Is this info correct? ")

    Stor_Prompt = (f"Write a holloween story where {Char_Name} is the main charactars name, {Char_Age} is their age, {Char_Fav_Candy} is their favorite candy, {Char_Trait} is a trait that the character has, {Char_FFact} is a fun fact avout the character, and {Stor_Local} is where the entire story takes place. And make sure that it is family friendly.")

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": Stor_Prompt}]
    )

    if check == ("y"):
        Story = response.choices[0].message.content
        print("\nGenerated Story:\n")
        print(Story)
        print(" ")
        save_choice = input("\nDo you want to download the story? ")

        if save_choice in ("y"):
            filename = input("Enter a filename (without extension): ").strip() + ".txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(Story)
            print(f"Story saved as {filename}")
        else:
            print("Story not saved.")
    else:
        restart = input("do you want to retry? ")
        if restart == ("y"):
            return
        elif restart == ("n"):
            print("Goodbye then!")
        else:
            print("Error")

Story()

#print(Char_Name)
#print(Char_Age)
#print(Char_Fav_Candy)
#print(Char_Trait)
#print(Char_FFact)
#print(Stor_Local)