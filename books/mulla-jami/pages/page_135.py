# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 135 (printed ١٣٤)."""

PAGE_NUMBER = 135
PRINTED_PAGE = "١٣٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "لا يعهد أن يطلق على ما وضع بإزاء شيء أنه قرينة عليه، فلا يرد[[١]] أن ذكر الإعراب مستغنى عنه؛ إذ القرينة شاملة له، وهي:",
     "en": "it is not customary to call what is coined to denote a thing an “indicator” of it — so it is no objection that mention of the inflection is dispensed with, since the [category of the] indicator is inclusive of it. And it is [of two kinds]:"},
    {"type": "matn",
     "ar": "١- إما لفظية، نحو: «ضربت موسى حبلى»[[٢]].",
     "en": "1 — Either verbal, as in ḍarabat Mūsā ḥublā (“a pregnant [woman] struck Mūsā”)."},
    {"type": "matn",
     "ar": "٢- أو معنوية، نحو: «أكل الكمثرى يحيى». (أو كان) الفاعل (مضمرا متصلا) بالفعل[[٣]]:",
     "en": "2 — Or meaning-based (maʿnawī), as in akala al-kummathrā Yaḥyā (“Yaḥyā ate the pears”). (Or the agent is a pronoun attached) to the verb:"},
    {"type": "matn",
     "ar": "١- بارزا كـ«ضربت زيدا».",
     "en": "1 — visible (bāriz), as in ḍarabtu Zaydan (“I struck Zayd”);"},
    {"type": "matn",
     "ar": "٢- أو مستكنا كـ«زيد ضرب غلامه»، بشرط أن يكون المفعول متأخرا عن الفعل؛ لئلا ينتقض بمثل: «زيدا ضربت».",
     "en": "2 — or latent (mustakinn), as in Zaydun ḍaraba ghulāmahu (“Zayd struck his slave-boy”) — on the condition that the object come after the verb, lest [the rule] be violated by the like of Zaydan ḍarabtu (“Zayd I struck”)."},
    {"type": "matn",
     "ar": "(أو وقع مفعوله) أي: مفعول الفاعل (بعد «إلا») بشرط توسطها بينهما[[٤]] في صورتي التقديم والتأخير[[٥]]، نحو: «ما ضرب زيد إلا عمرا» (أو) بعد (معناها) نحو: «إنما ضرب زيد عمرا» (وجب تقديمه[[٦]]) أي: تقديم الفاعل على المفعول في جميع هذه الصور[[٧]].",
     "en": "(Or its object falls) — that is: the object of [the verb having] the agent — (after “illā”), on the condition of its (illā’s) coming between the two, in both cases of fronting and postposing, as in mā ḍaraba Zaydun illā ʿAmran (“Zayd struck none but ʿAmr”); (or) after (its meaning [i.e. a restrictive equivalent of illā]), as in innamā ḍaraba Zaydun ʿAmran (“Zayd struck only ʿAmr”) — (then it is obligatory to place it [the agent] first), that is: to place the agent before the object in all of these cases."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "مع أن التعميم بعد التخصيص شائع.",
     "en": "Moreover, generalization after specification is common."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فإن القرينة فيه اتصال علامة الفاعل بالفعل. ومن القرائن اللفظية الإعراب الظاهر في تابع أحدهما أو كليهما، نحو: «ضرب موسى عيسى الظريف» أو اتصال ضمير الثاني بالأول، نحو: «ضرب فتاه موسى».",
     "en": "For the indicator in it is the attachment of the agent’s marker to the verb. Among the verbal indicators is the overt inflection appearing on a follower (tābiʿ) of one of the two [nouns] or of both, as in ḍaraba Mūsā ʿĪsā al-ẓarīfa (“the witty one struck / was struck by Mūsā [or] ʿĪsā”); or the attachment of a pronoun [belonging] to the second to the first, as in ḍaraba fatāhu Mūsā (“his youth struck Mūsā” / “Mūsā’s youth struck [him]”)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ليس المراد بالاتصال معنى اللغة بل المصطلح، وهو كون الضمير مما لا يستقل في التلفظ، فإذا كان الفاعل هكذا لا يصح تقديم المفعول عليه.",
     "en": "What is meant by “attachment” is not the lexical sense but the technical one, namely the pronoun’s being of the sort that cannot stand independently in utterance; so when the agent is thus, it is not valid to place the object before it."},
    {"type": "pair",
     "ar": "فلا يطلب لقوله «متصلا» صلة. ولا فائدة في قول الشارح: «بالفعل»، بل يوهم اختصاص الحكم بفاعل الفعل، وليس كذلك لجريانه في «رويد زيدا» مثلا.",
     "en": "So no complement is required for his word “attached.” And there is no benefit in the Commentator’s word “to the verb”; rather it gives the false impression that the ruling is restricted to the agent of a [true] verb, which is not so, since it applies also in ruwayda Zaydan (“go easy on Zayd”), for example."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: بعد «إلا» الواقعة بينهما في صورة التقديم الثابت والتأخير الذي يحكم بامتناعه، يعني: أن التقديم الثابت مشروط بتوسط «إلا» بينهما؛",
     "en": "That is: after “illā” which falls between the two, in the case of the established fronting and the postposing that is ruled to be precluded; meaning: that the established fronting is conditioned upon “illā” coming between the two;"},
    {"type": "pair",
     "ar": "إذ لو لم يتوسط، وقدم الفاعل على المفعول لزم الفصل بين أداة الاستثناء والمستثنى، وذلك غير جائز.",
     "en": "for if it did not come between them, and the agent were placed before the object, there would follow a separation between the particle of exception and the excepted term (mustathnā), which is impermissible."},
    {"type": "pair",
     "ar": "والتأخير الممتنع أيضا مشروط بتوسط «إلا» بينهما لما سيذكره قدس سره.",
     "en": "And the precluded postposing too is conditioned upon “illā” coming between the two, for [the reason] he — may his secret be sanctified — will mention."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: وجوب التقديم وامتناع التأخير الذي هو لازمه كلاهما مشروط بتوسط «إلا» لإفادة انقلاب المعنى في هذه الصورة.",
     "en": "That is: the obligation of fronting and the preclusion of postposing — which is its concomitant — are both conditioned upon “illā” coming between [them], because of its yielding an inversion of the meaning in this case."},
    {"type": "pair",
     "ar": "وأما في صورة تقديم المفعول مع «إلا»، فلا يلزم الانقلاب بحسب الظاهر إلا أنه غير مستحسن.",
     "en": "As for the case of fronting the object together with “illā,” inversion is not entailed on the face of it — except that it is not [stylistically] approved."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: على ما يكون بعد الفعل؛ إذ المقصود امتناع الفصل بينه وبين الفعل؛ فلا يرد «زيدا ضربت». فلو قال: وجب أن يليه لكان أوضح.",
     "en": "That is: [placing it first] over what comes after the verb; for what is intended is the preclusion of separating it from the verb; so Zaydan ḍarabtu is no objection. Had he said, “it is obligatory that it immediately follow it [the verb],” it would have been clearer."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لا يقال: لا حاجة إلى هذا القول في جزاء الشرط، فإن الشرط يدل على هذا؛ لأنا نقول: لما وقع البعد بين حرفي الشرط والجزاء توهم أن الجزاء متعلق بالأخير، فدفع هذا الوهم بذلك القول، أو نقول:",
     "en": "It is not to be said: there is no need for this statement in the apodosis of the conditional, since the protasis indicates it; because we say: since a distance occurred between the two particles of the protasis and the apodosis, it might be imagined that the apodosis attaches to the latter, so he warded off this imagining by that statement. Or we say:"},
]
