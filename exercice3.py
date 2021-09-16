
def decomposer(secondes):
    sec_annee = ((60*60)*24)*365
    sec_semaine = ((60*60)*24)*7
    sec_jours = ((60*60)*24)
    sec_heures = (60*60)
    sec_minutes = 60
    sec_sec = 1

    # TODO: Assigner à la variable "annees" le nombre d'années
    année_total = secondes/ sec_annee
    annees_dec = (année_total % 1)
    annees = int(année_total)


    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    sem_total = (annees_dec * sec_annee)/ sec_semaine
    sem_dec = (sem_total % 1)
    semaines = int(sem_total)

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours_total = (sem_dec * sec_semaine)/ sec_jours
    jours_dec = (jours_total % 1)
    jours = int(jours_total)

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures_total = (jours_dec * sec_jours)/ sec_heures
    heures_dec = (heures_total % 1)
    heures = int(heures_total)

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes_total = (heures_dec * sec_heures) / sec_minutes
    minutes_dec = (minutes_total % 1)
    minutes = int(minutes_total)

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes_total = (minutes_dec * sec_minutes)/ sec_sec
    sec_dec = (secondes_total % 1)
    secondes = int(secondes_total)

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)


if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
