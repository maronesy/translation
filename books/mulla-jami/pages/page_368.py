# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 368 (printed ٣٦٧)."""

PAGE_NUMBER = 368
PRINTED_PAGE = "٣٦٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وكان الأوفق بما سبق أن يقول: «لولا» from PDF p. 367.
    {"type": "matn",
     "ar": "أنا، لولا نحن إلى آخرها»، لكن غير الأسلوب تنبيها على أنه ليس بضروري[[١]]",
     "en": "…anā, lawlā naḥnu, to the end of them”; but he changed the manner of expression to signal that it is not necessary."},
    {"type": "matn",
     "ar": "(و) كذلك الأكثر في الاستعمال اتصال الضمير المرفوع بعد «عسى» لكون ما بعد «عسى» فاعلا، تقول: («عسيت» إلى آخرها[[٢]]).",
     "en": "(And) likewise the more common in usage is connection of the nominative pronoun after “ʿasā”, because what follows “ʿasā” is an agent; you say: (“ʿasayta” (perhaps you) to the end of them)."},
    {"type": "matn",
     "ar": "(وجاء) في بعض اللغات («لولاك» و«عساك» إلى آخرهما).",
     "en": "(There occurs) in some dialects (“lawlāka” and “ʿasāka” to the end of them)."},
    {"type": "matn",
     "ar": "فذهب الأخفش إلى أن الكاف بعد «لولا» ضمير مجرور وقع موقع المرفوع، فإن الضمائر قد يقع بعضها موقع بعض،",
     "en": "Al-Akhfash held that the kāf after “lawlā” is a genitive pronoun that has taken the place of the nominative, for pronouns sometimes take one another’s place,"},
    {"type": "matn",
     "ar": "كما تقول: «ما أنا كأنت» فـ«أنت» في هذا المقام مع أنه ضمير مرفوع وقع موقع المجرور.",
     "en": "as you say “mā anā ka-anta” (I am not like you): “anta” here, though a nominative pronoun, has taken the place of the genitive."},
    {"type": "matn",
     "ar": "وذهب سيبويه إلى أن «لولا» في هذا المقام[[٣]] حرف جر[[٤]]، والكاف ضمير مجرور واقع موقعه،",
     "en": "Sībawayh held that “lawlā” in this setting is a preposition, and the kāf is a genitive pronoun in its own proper place."},
    {"type": "matn",
     "ar": "فالأخفش تصرف فيما بعد «لولا»[[٥]]، وسيبويه في نفسه[[٦]].",
     "en": "So al-Akhfash made an adjustment in what follows “lawlā”, and Sībawayh in [“lawlā”] itself."},
    {"type": "matn",
     "ar": "وأما «عساك»، فذهب الأخفش إلى أنه ضمير منصوب واقع موقع المرفوع، وسيبويه إلى أن «عسى» محمول على «لعل» لتقاربهما في المعنى[[٧]]،",
     "en": "As for “ʿasāka”, al-Akhfash held that it is an accusative pronoun in the place of the nominative, and Sībawayh that “ʿasā” is treated like “laʿalla” because of their closeness in meaning."},
    {"type": "matn",
     "ar": "فههنا أيضا الأخفش تصرف في الضمير[[٨]]، وسيبويه في العامل.",
     "en": "So here too al-Akhfash made an adjustment in the pronoun, and Sībawayh in the governor."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ولو غيره إلى ما هو المتعارف في التعريف لكان أولى،",
     "en": "Had he changed it to what is customary in definitions, it would have been better;"},
    {"type": "pair",
     "ar": "وفي تعبيره مع فوت كمال الموافقة إيهام خروج ضميري المتكلم عن الحكم.",
     "en": "and his wording, besides missing complete consistency, suggests that the two first-person pronouns are excluded from the ruling."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إنما لم يقل: لولا أنت وعسيت إلى آخرهما لاختلاف الضميرين بالاتصال والانفصال.",
     "en": "He did not say “lawlā anta and ʿasayta to the end of them” only because the two pronouns differ in connection and separation."},
    {"type": "pair",
     "ar": "ولما لم يختلف الضميران في لولاك وعساك اعتبر لهما غاية واحدة.",
     "en": "Since the two pronouns do not differ in “lawlāka” and “ʿasāka”, he assigned them a single endpoint."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: في مقام اتصال الضمير خاصة.",
     "en": "That is, specifically where the pronoun is connected."},
    {"type": "pair",
     "ar": "قال سيبويه: يصح أن يكون لبعض الكلمات مع بعضها حال كما أن لدن تجر ما بعدها بالإضافة، وإذا وليتها غدوة تنصبها.",
     "en": "Sībawayh said: some words may have a [special] state with certain others, just as “ladun” puts what follows it in the genitive by annexation, but when “ghudwatan” follows it, it puts it in the accusative."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: فيه نظر؛ لأن الجار إذا لم يكن زائدا لا بد له من متعلق، ومتعلقه غير ظاهر.",
     "en": "Shaykh al-Raḍī said: this is open to question, because a preposition that is not redundant must have something to which it attaches, and what it attaches to is not apparent."},
    {"type": "pair",
     "ar": "ويمكن أن يقال: متعلقه جوابه؛ إذ معنى لولاك لهلكت: انتفى هلاكي لوجودك.",
     "en": "It could be said: what it attaches to is its apodosis, since the meaning of “lawlāka la-halaktu” (were it not for you I would have perished) is “my perishing was prevented by your existence”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كأنه جعله في حكم حرف الجر ومحمولا عليه، فإنه في معنى اللام التعليلية",
     "en": "It is as though he treated it as having the status of a preposition and modelled on it, for it has the meaning of the causal lām;"},
    {"type": "pair",
     "ar": "كان قوله: لولاك لكان كذا في معنى لم يكن كذا لوجودك.",
     "en": "his saying “lawlāka la-kāna kadhā” (were it not for you, such would have been) means “such was not, because of your existence”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ويلزمه تغيير اثني عشر ضميرا.",
     "en": "This obliges him to alter twelve pronouns."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يرجحه أن التغيير في واحد.",
     "en": "What favours it is that the alteration is in one [word]."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لأن معناهما الإطماع والإشفاق، فيراعي جانبي «لعل وعسى»، فينصب الاسم به، فيجعل خبره مضارعا البتة.",
     "en": "Because their meaning is arousing hope and apprehension; so he observes both sides, “laʿalla” and “ʿasā”: he puts the noun in the accusative by it, and makes its predicate an imperfect verb without exception."},
    {"type": "pair",
     "ar": "والغالب فيه أن يكون مع أن لرعاية «عسى»، وجاز تركه لرعاية «لعل».",
     "en": "Usually it comes with “an”, in observance of “ʿasā”, and omitting it is permitted in observance of “laʿalla”."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "والتصرف فيه لكونه معمولا أولى؛ لأن المعمول محل التصرف، وكذا لكونه متأخرا؛ لأن التأويل في المتأخر تأويل عند الحاجة.",
     "en": "Adjusting it is preferable because it is the governed word, the governed word being the locus of adjustment; and likewise because it comes later, since interpreting what comes later is interpreting at the point of need."},
]
