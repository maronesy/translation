# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 527 (printed ٥٢٦)."""

PAGE_NUMBER = 527
PRINTED_PAGE = "٥٢٦"   # Arabic-Indic, as printed

BLOCKS = [
    # PDF p. 526 ends with a complete sentence.
    {"type": "section", "ar": "[أفعال المقاربة]",
     "en": "The Verbs of Appropinquation (afʿāl al-muqāraba)"},

    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(أفعال المقاربة: ما وضع) أي: فعل وضع (لدنو الخبر) أي: للدلالة على قرب حصوله للفاعل",
     "en": "(The verbs of appropinquation are what was coined), that is, a verb coined, (for the nearness of the predicate), that is, to indicate the nearness of its occurring for the agent,"},
    {"type": "matn",
     "ar": "(رجاء) منصوب على المصدرية بتقدير مضاف، أي دنو رجاء، بأن يكون ذلك الدنو بحسب رجاء المتكلم، وطمعه حصول الخبر له، لا بجزمه به.",
     "en": "(by way of hope): it is in the accusative as a verbal noun, with a first term of a genitive construction supplied, that is, “a nearness of hope”, in that this nearness is according to the speaker’s hope and his eager expectation that the predicate will occur for it, not according to his certainty of it."},
    {"type": "matn",
     "ar": "فعسى في قولك: عسى زيد أن يخرج يدل على قرب حصول الخروج لزيد، بسبب أنك ترجو ذلك وتطمعه، لا أنك جازم به.",
     "en": "So “ʿasā” in your saying “ʿasā Zaydun an yakhruja” (perhaps Zayd will go out) indicates the nearness of going out occurring for Zayd, because you hope for it and expect it eagerly, not because you are certain of it."},
    {"type": "matn",
     "ar": "(أو) وضع لدنو الخبر وقرب ثبوته للفاعل (حصولا) أي: دنو حصول، بأن يكون إخبار المتكلم بذلك الدنو لإشراف الخبر على حصوله للفاعل،",
     "en": "(Or) coined for the nearness of the predicate and the proximity of its holding for the agent (by way of occurrence), that is, “a nearness of occurrence”, in that the speaker’s report of this nearness is because the predicate is on the verge of occurring for the agent;"},
    {"type": "matn",
     "ar": "فـ«كاد» في قولك: «كاد زيد أن يخرج» تدل على قرب حصول الخروج لزيد لجزمك بقرب حصوله.",
     "en": "so “kāda” in your saying “kāda Zaydun an yakhruja” (Zayd was about to go out) indicates the nearness of going out occurring for Zayd, because of your certainty that its occurrence is near."},
    # REVIEW: printed «لما يفضى إليه» with final ى here, but «فيما يفضي إليه» later in the same passage. Transcribed as printed.
    {"type": "matn",
     "ar": "(أو) وضع لدنو الخبر وقرب حصوله للفاعل (أخذا فيه) أي: دنو أخذ وشروع في الخبر، بأن يكون ذلك الدنو بسبب جزم المتكلم بشروع الفاعل في الخبر بالتصدي لما يفضى إليه،",
     "en": "(Or) coined for the nearness of the predicate and the proximity of its occurring for the agent (by way of setting about it), that is, “a nearness of setting about and commencing the predicate”, in that this nearness is due to the speaker’s certainty that the agent has commenced the predicate by undertaking what leads to it;"},
    {"type": "matn",
     "ar": "فـ«طفق» في قولك: «طفق زيد يخرج» يدل على قرب حصول الخروج لزيد بسبب جزم المتكلم بشروعه فيما يفضي إليه.",
     "en": "so “ṭafiqa” in your saying “ṭafiqa Zaydun yakhruju” (Zayd began to go out) indicates the nearness of going out occurring for Zayd, because of the speaker’s certainty that he has commenced what leads to it."},
    {"type": "matn",
     "ar": "(فالأول) أي: ما وضع لدنو الخبر رجاء («عسى») قال سيبويه: «عسى» طمع وإشفاق[[١]]،",
     "en": "(The first), that is, what was coined for the nearness of the predicate by way of hope, (is “ʿasā”). Sībawayh said: “ʿasā” is eager hope and apprehension (ishfāq);"},
    {"type": "matn",
     "ar": "فالطمع في المحبوب، والإشفاق في المكروه، نحو: «عسيت أن أموت»، ومعنى الإشفاق: الخوف",
     "en": "eager hope concerns what is loved, and apprehension concerns what is disliked, as in “ʿasaytu an amūta” (it may be that I die); the meaning of ishfāq is fear."},
    {"type": "matn",
     "ar": "(وهو غير متصرف) حيث لا يجيء[[٢]] منه مضارع، ومجهول، وأمر، ونهي، إلى غير ذلك من الأمثلة،",
     "en": "(And it is not inflected [ghayr mutaṣarrif]), in that no imperfect, passive, imperative, prohibitive or other such forms come from it."},
    {"type": "matn",
     "ar": "وإنما لم يتصرف في «عسى» لتضمنه إنشاء الطمع والرجاء[[٣]] كـ«لعل» والإنشآت في الأغلب[[٤]] من معاني الحروف، والحروف لا يتصرف فيها.",
     "en": "“ʿAsā” is not inflected only because it contains the performative expression (inshāʾ) of eager hope and hope, like “laʿalla”; performatives are for the most part among the meanings of particles, and particles are not inflected."},
    {"type": "matn",
     "ar": "(تقول) على أحد استعماليه («عسى زيد أن يخرج») وهو أن يكون بعده اسم، ثم فعل مضارع مصدر بـ«أن» الاستقبالية تقوية لمعنى الترجي الذي هو توقع وجود الفعل",
     "en": "(You say), according to one of its two uses, (“ʿasā Zaydun an yakhruja”), namely that a noun follows it and then an imperfect verb headed by the future “an”, to strengthen the sense of hoping (tarajjī), which is the expectation of the action’s occurring…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيخرج عن تعريف أفعال المقاربة «عسى» للإشفاق، فينبغي أن يقول: رجاء أو إشفاق،",
     "en": "So “ʿasā” used for apprehension falls outside the definition of the verbs of appropinquation, and he ought to have said “by way of hope or apprehension”."},
    # REVIEW: printed «موضوعة لدنو لخبر رجاء»; «لدنو الخبر» seems intended. Transcribed as printed.
    {"type": "pair",
     "ar": "لا تقول: عسى الإشفاقية موضوعة لدنو لخبر رجاء؛ لأنا نقول: قيد الحيثية مراد،",
     "en": "Do not say: “ʿasā” of apprehension is coined for the nearness of the predicate by way of hope; for we say: the qualification “in so far as” is intended."},
    {"type": "pair",
     "ar": "وكيف لا، وأفعال المقاربة قد يكون لبعضها معنى لا يكون باعتباره منها.",
     "en": "How could it not be, when some of the verbs of appropinquation sometimes have a meaning in respect of which they are not among them?"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «فإنه لم يجيء» (with ي after «لم»); transcribed as printed.
    {"type": "pair",
     "ar": "إلا أنه متصرف في نفسه، فإنه لم يجيء منه صيغ الماضي كلها.",
     "en": "Except that it is inflected within itself, for not all the forms of the perfect come from it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أو الإشفاق.",
     "en": "Or apprehension."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إنما قال: في الأغلب: لأن أمثال «اضرب» إنشاء لكنها مع كثرتها مغلوبة للحروف الإنشائية.",
     "en": "He said “for the most part” only because forms such as “iḍrib” (strike!) are performatives, but despite their number they are outweighed by the performative particles."},
]
