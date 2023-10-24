from app import app
from init import db
from models import User, Post, Tag, PostTag

with app.app_context():
    db.drop_all()
    db.create_all()

users = [
    User(
        first_name="John",
        last_name="Wick",
        image_url="https://avatarfiles.alphacoders.com/336/336452.jpg",
    ),
    User(
        first_name="Mace",
        last_name="Windu",
        image_url="https://comicvine.gamespot.com/a/uploads/scale_medium/11122/111226069/4817468-6565664823-tumbl.jpg",
    ),
    User(
        first_name="Anakin",
        last_name="Skywalker",
        image_url="https://i.redd.it/vwm1lqdtymj91.jpg",
    ),
    User(
        first_name="John",
        last_name="Nolan",
        image_url="https://tv-fanatic-res.cloudinary.com/iu/s--faBe1hrA--/t_full/cs_srgb,f_auto,fl_strip_profile.lossy,q_auto:420/v1679686940/john-nolan-the-rookie-s5e19.png",
    ),
    User(
        first_name="Naruto",
        last_name="Uzumaki",
        image_url="https://comicvine.gamespot.com/a/uploads/scale_medium/11117/111178336/5603895-dcc2d502-6c35-49c9-c93c-6eae7f44d551.jpg",
    ),
    User(
        first_name="Hera",
        last_name="Syndulla",
        image_url="https://upload.wikimedia.org/wikipedia/en/e/e3/Hera_Syndulla_Ahsoka.jpg",
    ),
    User(
        first_name="Bo-Katan",
        last_name="Kryze",
        image_url="https://i.redd.it/0d2d1q6qm0k61.jpg",
    ),
    User(
        first_name="Ahsoka",
        last_name="Tano",
        image_url="https://i.redd.it/4spfxs2x0ie61.jpg",
    ),
    User(first_name="Ghost", last_name="Unknown"),
]

posts = [
    Post(
    title="The Force",
    content="The Force was an energy field created by all life that bound everything in the universe together. It was known by a variety of names throughout galactic history: It was called the Ashla by the Lasats, It by the dianoga Omi, the Life Current by the Mustafarians, the Tide by the Lew'elans, the Sight by the Chiss, the Life Wind by the Zeffonians, the Great Presence by the Pathfinders of the Chaos, the Luminous Mist by the Mist-Weavers, the Unity by the Sorcerers of Tund, and as the Beyond by the Magys and her people. The Force was created by life, and therefore it resided in all life forms. It was especially powerful in a select group of individuals who were born with a high concentration of midi-chlorians—microscopic, intelligent lifeforms that formed a symbiotic relationship with and communicated the will of the Force to their host—in their blood. These people were deemed Force-sensitive, and were capable of consciously sensing the Force. With this conscious sense of the Force came the ability to harness it, allowing Force-sensitives to access various Force powers. Unlike organic beings, droids and other artificial constructs existed outside of the Force. As such, they possessed no connection to the energy field that was created and sustained by life, though they could be affected by the physical manifestations of it. Apart from its scientific aspect, the Force was the basis of various religious organizations, who held differing views as to the nature and purpose of the Force. These included the Church of the Force, the Guardians of the Whills, and most notably the Jedi and Sith Orders. In addition, the Lasats believed that the Force was the 'spirit' of the galaxy.",
    user_id=8,
),
    Post(
        title = "Madalore",
        content = """Mandalore, also known as Mand'alor, was a planet located in the Outer Rim Territories. It was the homeworld of the Mandalorians, a fearsome warrior clan-based people, and the indigenous Alamite species. The Mandalorians once fought the Jedi and raided their temple during the fall of the Old Republic. Wearing distinctive armor that was often made from beskar, they were feared throughout the galaxy, and once had political influence over two thousand other star systems.

Many years of war left the planet inhospitable, forcing the Mandalorians to live within domed cities. A pacifist regime came to power at the end of these wars, led by Duchess Satine Kryze, who joined the Galactic Republic. The Mandalorian Civil War was fought between the pacifists and the martial traditionalists. The Civil War ended in a victory for the New Mandalorians, and those who refused to give up their warrior ways were exiled to the moon Concordia, and believed to have died out.

During the Clone Wars, the New Mandalorians were overthrown by the renegade Sith Lord Maul's Shadow Collective, whose forces included the Death Watch, which was formed from the exiled warriors. A new civil war soon erupted between the Mandalore resistance, which had the aid of the Republic, and the forces of the Shadow Collective. The resulting siege by a Mandalorian-Republic joint force ended Maul's rule over the planet. The Republic subsequently appointed Bo-Katan Kryze, the leader of the Mandalore resistance, as Regent of Mandalore. However, Kryze's rule was soon ended by Gar Saxon and his clan, who betrayed Kryze and pledged loyalty to the Republic's successor state, the Galactic Empire. For his loyalty, Saxon was appointed Viceroy and Governor of Mandalore, which was now under Imperial occupation.""",
        user_id = 7
    ),
    Post(
        title='Anakin',
        content='''Anakin Skywalker was a legendary Force-sensitive human male who was a Jedi Knight of the Galactic Republic and the prophesied Chosen One of the Jedi Order, destined to bring balance to the Force. Also known as "Ani" during his childhood, Skywalker earned the moniker "Hero With No Fear" from his accomplishments in the Clone Wars. His alter ego, Darth Vader, the Dark Lord of the Sith, was created when Skywalker turned to the dark side of the Force, pledging his allegiance to the Sith Lord Darth Sidious at the end of the Republic Era.

A vergence in the Force, Anakin Skywalker was born on the desert planet of Tatooine in the Outer Rim Territories in 41 BBY. He was the son of Shmi Skywalker, a slave who conceived a child without a father. His blood contained over twenty-thousand midi-chlorians, surpassing Grand Master Yoda and all other Jedi in the galaxy. Qui-Gon Jinn, the Jedi Master who discovered Skywalker during the Invasion of Naboo in 32 BBY, theorized that Skywalker was conceived by the midi-chlorians. Following the Battle of Naboo, the Jedi High Council admitted Anakin Skywalker into the Order as the Padawan of Jedi Knight Obi-Wan Kenobi despite feeling that he was too old and emotional to adhere to the Jedi Code. Skywalker remained a Padawan through the beginning of the Clone Wars, instigated by events set in motion by Count Dooku. Although Jedi doctrine prohibited personal relationships, Anakin Skywalker had a secret wife, Senator Padmé Amidala of Naboo. During the early days of the Clone Wars, Skywalker served as a Jedi General in the Grand Army of the Republic, commanding the clone troopers of the elite 501st Legion against the Confederacy of Independent Systems. After receiving his knighthood, Skywalker oversaw the Jedi training of his own apprentice, Ahsoka Tano. By 19 BBY, when Tano walked away from the Jedi Order, Skywalker began to struggle with feelings of failure towards his apprentice and the Order itself.''',
        user_id=3
    )
]

tags = [
    Tag(name='the force'),
    Tag(name='for mandalore'),
    Tag(name='jedi'),
    Tag(name='lightsaber'),
    Tag(name='house of kryse')
]

posttag = [
    PostTag(post_id='1', tag_id='1'),
    PostTag(post_id='1', tag_id='3'),
    PostTag(post_id='1', tag_id='4'),
    PostTag(post_id='2', tag_id='2'),
    PostTag(post_id='2', tag_id='5'),
    PostTag(post_id='3', tag_id='1'),
    PostTag(post_id='3', tag_id='3'),
    PostTag(post_id='3', tag_id='4'),

]
with app.app_context():
    db.session.add_all(users)
    db.session.commit()
    db.session.add_all(posts)
    db.session.commit()
    db.session.add_all(tags)
    db.session.commit()
    db.session.add_all(posttag)
    db.session.commit()
