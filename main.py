import textwrap

from mcq_app.mcq_generation import MCQGenerator


def show_result(generated: str, answer: str, context:str, original_question: str = ''):
    
    print('Context:')

    for wrap in textwrap.wrap(context, width=120):
        print(wrap)
    print()

    print('Question:')
    print(generated)

    print('Answer:')
    print(answer)
    print('-----------------------------')


MCQ_Generator = MCQGenerator(True)

context_a = '''The koala or, inaccurately, koala bear[a] (Phascolarctos cinereus), is an arboreal herbivorous 
marsupial native to Australia. It is the only extant representative of the family Phascolarctidae and its closest
 living relatives are the wombats, which are members of the family Vombatidae. The koala is found in coastal areas
  of the mainland's eastern and southern regions, inhabiting Queensland, New South Wales, Victoria, and South 
  Australia. It is easily recognisable by its stout, tailless body and large head with round, fluffy ears and 
  large, spoon-shaped nose. The koala has a body length of 60–85 cm (24–33 in) and weighs 4–15 kg (9–33 lb). 
  Fur colour ranges from silver grey to chocolate brown. Koalas from the northern populations are typically 
  smaller and lighter in colour than their counterparts further south. These populations possibly are separate 
  subspecies, but this is disputed.'''

context_oxygen = '''Oxygen is the chemical element with the symbol O and atomic number 8. It is a member of the 
chalcogen group in the periodic table, a highly reactive nonmetal, and an oxidizing agent that readily forms 
oxides with most elements as well as with other compounds. Oxygen is Earth's most abundant element, and after 
hydrogen and helium, it is the third-most abundant element in the universe. At standard temperature and 
pressure, two atoms of the element bind to form dioxygen, a colorless and odorless diatomic gas with the 
formula O
2. Diatomic oxygen gas currently constitutes 20.95% of the Earth's atmosphere, though this has changed 
considerably over long periods of time. Oxygen makes up almost half of the Earth's crust in the form of oxides.[3]


Dioxygen provides the energy released in combustion[4] and aerobic cellular respiration,[5] and many major 
classes of organic molecules in living organisms contain oxygen atoms, such as proteins, nucleic acids, 
carbohydrates, and fats, as do the major constituent inorganic compounds of animal shells, teeth, and bone. 
Most of the mass of living organisms is oxygen as a component of water, the major constituent of lifeforms. 
Oxygen is continuously replenished in Earth's atmosphere by photosynthesis, which uses the energy of sunlight 
to produce oxygen from water and carbon dioxide. Oxygen is too chemically reactive to remain a free element 
in air without being continuously replenished by the photosynthetic action of living organisms. Another form 
(allotrope) of oxygen, ozone (O
3), strongly absorbs ultraviolet UVB radiation and the high-altitude ozone layer helps protect the biosphere 
from ultraviolet radiation. However, ozone present at the surface is a byproduct of smog and thus a pollutant.

Oxygen was isolated by Michael Sendivogius before 1604, but it is commonly believed that the element was 
discovered independently by Carl Wilhelm Scheele, in Uppsala, in 1773 or earlier, and Joseph Priestley in 
Wiltshire, in 1774. Priority is often given for Priestley because his work was published first. Priestley, 
however, called oxygen "dephlogisticated air", and did not recognize it as a chemical element. The name oxygen 
was coined in 1777 by Antoine Lavoisier, who first recognized oxygen as a chemical element and correctly 
characterized the role it plays in combustion.

Common uses of oxygen include production of steel, plastics and textiles, brazing, welding and cutting of steels 
and other metals, rocket propellant, oxygen therapy, and life support systems in aircraft, submarines, spaceflight
 and diving.'''
context_pulchowk = '''Renewable energy sources have gained significant attention in recent years due to their 
potential to mitigate the adverse effects of traditional fossil fuels on the environment. The shift towards 
renewable energy is driven by concerns over climate change, air pollution, and the finite nature of fossil fuel 
resources.

One prominent form of renewable energy is solar power. Solar panels, which harness energy from the sun, have become
 increasingly affordable and efficient. They offer a clean and sustainable alternative to traditional electricity 
 generation methods that rely on burning fossil fuels. The adoption of solar power has led to reduced greenhouse 
 gas emissions and a lower environmental impact.

Wind energy is another key player in the renewable energy sector. Wind turbines generate electricity by harnessing
 the power of the wind. As technology advances, wind farms have become more efficient and capable of producing larger amounts of clean energy. The expansion of wind energy contributes to a diversified energy portfolio and a reduced reliance on non-renewable resources.

Hydropower, derived from the energy of moving water, is a longstanding and reliable source of renewable energy. 
Dams and other water infrastructure can generate electricity without emitting greenhouse gases. While hydropower 
has proven to be effective, concerns have been raised about its environmental impact on aquatic ecosystems and local communities.

In addition to these sources, advancements in bioenergy, geothermal energy, and tidal power are further expanding 
the renewable energy landscape. Governments, businesses, and individuals worldwide are investing in these 
sustainable alternatives to address the global energy challenge.

The transition to renewable energy is not without challenges. Initial costs of installing renewable energy 
infrastructure can be high, and there are intermittency issues with certain sources like solar and wind. 
However, ongoing research and technological advancements aim to address these challenges and make renewable 
energy more accessible and reliable.

In conclusion, the adoption of renewable energy sources has the potential to revolutionize the way we generate 
power, offering a cleaner and more sustainable future. As technology continues to evolve, the environmental 
benefits of renewable energy will likely become even more pronounced, contributing to a healthier planet for 
generations to come.'''

context_lol = ''' 
In the heart of history, students at the secondary level embark on a journey to unravel the tales of the past. From ancient civilizations to modern revolutions, they explore the events and figures that have shaped our world. Through in-depth studies, students analyze the causes and consequences of historical events, gaining insights into the triumphs and challenges faced by societies throughout time. They examine the political movements, cultural shifts, and technological advancements that have left an indelible mark on humanity. As they navigate the historical landscape, students not only absorb facts and dates but also cultivate critical thinking skills to interpret and evaluate different perspectives. History becomes a living narrative, inviting students to connect with the past and draw lessons for the present and future
'''
MCQ_Generator.generate_mcq_questions(context_lol, 8)
