# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 283 (printed ٢٨٢)."""

PAGE_NUMBER = 283
PRINTED_PAGE = "٢٨٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وهو) أي: والحال أن المستثنى واقع (في غير) الكلام» from PDF p. 282.
    {"type": "matn",
     "ar": "(الموجب) واشترط ذلك (ليفيد) فائدة صحيحة[[١]] (مثل: «ما ضربني إلا زيد»[[٢]])؛ إذ يصح ألا يضرب المتكلم أحد إلا زيدا،",
     "en": "…(affirmative). He stipulated this (so that it conveys) a sound benefit, (as in “No one struck me except Zayd”), since it is valid that no one struck the speaker except Zayd;"},
    {"type": "matn",
     "ar": "بخلاف «ضربني إلا زيد»؛ إذ لا يصح أن يضرب كل أحد المتكلم إلا زيدا",
     "en": "unlike “There struck me except Zayd,” since it is not valid that everyone struck the speaker except Zayd,"},
    {"type": "matn",
     "ar": "(إلا أن يستقيم المعنى[[٣]]) بأن يكون الحكم مما يصح أن يثبت على سبيل العموم نحو قولك: «كل حيوان[[٤]] يحرك فكه الأسفل عند المضغ إلا التمساح»،",
     "en": "(unless the meaning holds), in that the judgement is one that can validly hold universally, as in your saying: “Every animal moves its lower jaw when chewing, except the crocodile”;"},
    {"type": "matn",
     "ar": "أو يكون هناك قرينة دالة على أن المراد بالمستثنى منه بعض معين يدخل فيه المستثنى قطعا",
     "en": "or there is an indication (qarīna) there that what is meant by the mustathnā minhu is a specific part in which the excepted term is certainly included,"},
    {"type": "matn",
     "ar": "(مثل: «قرأت إلا يوم كذا») أي: أوقعت القراءة كل يوم إلا يوم كذا، لظهور أنه لا يريد المتكلم جميع أيام الدنيا، بل أيام الأسبوع أو الشهر أو مثل ذلك.",
     "en": "(as in “I read except on such-and-such a day”), that is, I did the reading every day except such-and-such a day; for it is evident that the speaker does not mean all the days of the world, but the days of the week or the month or the like."},
    {"type": "matn",
     "ar": "ولقائل أن يقول: كما لا يستقيم المعنى على تقدير عموم المستثنى منه في الموجب في بعض الصور، فربما لا يستقيم المعنى على تقدير عموم المستثنى منه في غير الموجب أيضا نحو: «ما مات إلا زيد»،",
     "en": "Someone may say: just as the meaning does not hold, on the supposition that the mustathnā minhu is general, in affirmative speech in some cases, so the meaning may also fail to hold, on the supposition that the mustathnā minhu is general, in non-affirmative speech, as in “No one died except Zayd”;"},
    {"type": "matn",
     "ar": "فينبغي أن يشترط في غير الموجب أيضا استقامة المعنى،",
     "en": "so the soundness of the meaning ought to be stipulated in non-affirmative speech as well."},
    {"type": "matn",
     "ar": "وأيضا لا يصح مثل: «قرأت إلا يوم كذا» إلا بعد تخصيص اليوم بأيام الأسبوع مثلا،",
     "en": "Further, such as “I read except on such-and-such a day” is valid only after “day” has been restricted to the days of the week, for example;"},
    {"type": "matn",
     "ar": "فيجوز مثل هذا التخصيص في «ضربني إلا زيد» بأن يتخصص المستثنى منه بكل واحد من جماعة مخصوصين إذا كان هناك قرينة،",
     "en": "so the like of this restriction is permissible in “There struck me except Zayd,” in that the mustathnā minhu is restricted to each one of a particular group, when there is an indication there;"},
    {"type": "matn",
     "ar": "فلا فرق بين هاتين الصورتين في كون كل واحدة منهما جائزة مع القرينة وغير جائزة بدونها.",
     "en": "so there is no difference between these two cases in that each of them is permissible with an indication and impermissible without it."},
    {"type": "matn",
     "ar": "وأجيب: بأن المعتبر هو الغالب، والغالب في الإيجاب عدم استقامة المعنى على العموم، وفي النفي عكسه؛",
     "en": "It has been answered that what counts is the predominant case: what predominates in affirmation is that the meaning does not hold on generality, and in negation the reverse;"},
    {"type": "matn",
     "ar": "لأن اشتراك جميع أفراد الجنس في انتفاء تعلق الفعل بها، ومخالفة واحد إياها في ذلك مما يكثر ويغلب.",
     "en": "because all the members of a genus sharing in the absence of the action’s connection with them, and one [member] differing from them in that, is something frequent and predominant."},
    {"type": "matn",
     "ar": "وأما اشتراكها في تعلق الفعل بها ومخالفة واحد إياها في ذلك فمما يقل، كما في المثال المذكور،",
     "en": "As for their sharing in the action’s connection with them, and one differing from them in that, it is among what is rare, as in the example mentioned;"},
    {"type": "matn",
     "ar": "وبأن الفرق بين قولك: «قرأت إلا يوم كذا» و«ضربني إلا زيد» ليس إلا بظهور قرينة دالة على بعض",
     "en": "and [it has been answered] that the difference between your saying “I read except on such-and-such a day” and “There struck me except Zayd” lies only in the presence of an indication pointing to a certain…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: ليفيد الكلام فائدة صحيحة.",
     "en": "He means: so that the speech conveys a sound benefit."},
    {"type": "pair",
     "ar": "ولك أن تقول: ليفيد المستثنى ما هو فائدة من جعل الكلام صادقا؛ إذ بالاستثناء من الكلام الموجب لا يصير الكلام صادقا بخلاف المنفي.",
     "en": "You may say: so that the excepted term conveys what is a benefit, by making the speech true; since through exception from affirmative speech the speech does not become true, unlike negative [speech]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يحتمل أن يكون فاعل «يفيد».",
     "en": "It may be the agent of “yufīd” (conveys)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: print reads «للنحوى» with final alif maqṣūra (for «للنحوي»); transcribed as printed.
    {"type": "pair",
     "ar": "قيل: لا بحث للنحوى عن استقامة المعنى إنما وظيفته بيان الكيفيات التركيبية، فهذا البحث من قبيل وضع الشيء في غير محله.",
     "en": "It has been said: the grammarian has no concern with the soundness of meaning; his task is only to set out the modes of construction. So this discussion is a case of putting a thing out of its place."},
    {"type": "pair",
     "ar": "قلت: مآل بحثه هذا أن الإعراب على حسب العوامل في كلام غير موجب كثير بخلاف الموجب، فإنه قليل لقلة استقامة المعنى فيه إذا أعرب المستثنى كذلك،",
     "en": "I say: the upshot of this discussion of his is that inflection according to the governors is frequent in non-affirmative speech, unlike affirmative speech, where it is rare because the meaning seldom holds in it when the excepted term is inflected in that way;"},
    {"type": "pair",
     "ar": "والبحث عن كثرة الاستعمال وقلته وظيفة الفن.",
     "en": "and the discussion of frequency and rarity of usage is the task of the discipline."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "مثال لما يصح فيه الحكم على سبيل العموم لا لما نحن فيه.",
     "en": "An example of what admits the judgement universally, not of what we are dealing with."},
]
