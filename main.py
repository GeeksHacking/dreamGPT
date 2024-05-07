from dreamGPT.dreamgpt.constants import MAX_ITERATIONS
from dreamGPT.dreamgpt.engine.dreamEngine import DreamEngine

def main(theme):
    all_dreams = []
    dreams = []
    engine = DreamEngine()
    themeSeeds = engine.expandTheme(theme)
    maxIterations = MAX_ITERATIONS
    while maxIterations > 0:
        iterations_dreams = {
            "seeds": [],
            "dreams": []
        }
        newDreams = engine.dream(themeSeeds)
        iterations_dreams["seeds"] = themeSeeds
        combinedDreams = engine.combine(newDreams + dreams)
        dreams = (engine.pick(combinedDreams + newDreams + dreams))
        for dream in dreams:
            my_json_object = {
                "title": dream.title,
                "description": dream.description,
                "noveltyScore": dream.noveltyScore,
                "marketScore": dream.marketScore,
                "usefulnessScore": dream.usefulnessScore,
                "easeOfImplementationScore": dream.easeOfImplementationScore,
                "impactScore": dream.impactScore,
            }
            iterations_dreams['dreams'].append(my_json_object)
        
        all_dreams.append(iterations_dreams)
               
        maxIterations -= 1
    return all_dreams
