# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 184 (printed ١٨٣)."""

PAGE_NUMBER = 184
PRINTED_PAGE = "١٨٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "لأن «ما فعله الفاعل» هو المعنى[[١]]، والمفعول المطلق من أقسام اللفظ، ويدخل فيه المصادر كلها[[٢]].",
     "en": "…because “what the agent did” is the meaning, whereas the absolute object belongs to the divisions of the utterance (lafẓ); and all verbal nouns (maṣādir) are included in it."},
    {"type": "matn",
     "ar": "(مذكور) صفة للفعل، وهو أعم[[٣]] من أن يكون مذكورا حقيقة، كما إذا كان مذكورا بعينه، نحو: «ضربته ضربا»",
     "en": "(Mentioned) is an adjective of “verb”; and it is more general than its being mentioned in reality—as when it is mentioned in its own form, as in “I beat him a beating” (ḍarabtuhu ḍarban)—"},
    {"type": "matn",
     "ar": "أو حكما كما إذا كان مقدرا نحو: ﴿فضرب الرقاب﴾[[٤]]، أو اسما[[٥]] فيه معنى الفعل، نحو: «ضارب ضربا»،",
     "en": "or by assimilated status, as when it is supplied by supposition, as in “then [strike] the striking of the necks” (fa-ḍarba al-riqābi), or a noun containing the meaning of the verb, as in “one who beats a beating” (ḍāribun ḍarban)."},
    {"type": "matn",
     "ar": "وخرج به المصادر التي لم يذكر فعلها لا حقيقة ولا حكما، نحو: «الضرب واقع على زيد».",
     "en": "By it are excluded the verbal nouns whose verb is not mentioned, neither in reality nor by assimilated status, as in “The beating fell upon Zayd” (al-ḍarbu wāqiʿun ʿalā Zaydin)."},
    {"type": "matn",
     "ar": "(بمعناه) صفة ثانية[[٦]] للفعل، وليس المراد به أن الفعل كائن بمعنى ذلك الاسم، فإن معنى الاسم جزء معناه،",
     "en": "(In its meaning) is a second adjective of “verb.” What is meant by it is not that the verb has the meaning of that noun, for the meaning of the noun is part of its [the verb’s] meaning;"},
    {"type": "matn",
     "ar": "بل المراد أن معنى الفعل مشتمل عليه[[٧]] اشتمال الكل",
     "en": "rather, what is meant is that the meaning of the verb contains it, as the whole contains…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لقائل أن يقول: لو لم يزد لصح أيضا؛ لأنهم يجرون صفات المدلولات المطابقية على دوالها كما في سائر حدود المفاعيل.",
     "en": "Someone may say: had it not been added, [the definition] would still have been valid, because they apply the attributes of meanings signified by full correspondence (al-madlūlāt al-muṭābaqiyya) to the expressions that signify them, as in the other definitions of the objects."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وغيرها مما في حكمها كالويل بمعنى الهلاك،",
     "en": "And others that share their status, like “al-wayl” in the sense of perdition."},
    {"type": "pair",
     "ar": "أراد بالمصدر اسم الحدث الجاري على الفعل.",
     "en": "By “verbal noun” (maṣdar) he meant the noun of the event (ism al-ḥadath) that runs parallel to the verb."},
    {"type": "pair",
     "ar": "وإنما سمي به؛ لأنه من صدر إذا رجع، وهو محل رجوع الفعل إليه لأخذه منه على مذهب البصرية، أو محل رجوعه إلى الفعل على مذهب الكوفية.",
     "en": "It was so named only because it is from ṣadara, “to return”: it is the place to which the verb returns, since [the verb] is taken from it, according to the doctrine of the Baṣrans; or the place from which it returns to the verb, according to the doctrine of the Kūfans."},
    {"type": "pair",
     "ar": "وقد يطلق على المفعول المطلق؛ لأنه في الغالب مصدر.",
     "en": "It is sometimes applied to the absolute object, because [the latter] is for the most part a verbal noun."},
    {"type": "pair",
     "ar": "وإنما قلنا: في الغالب؛ لأنه قد لا يكون مصدرا.",
     "en": "We said “for the most part” only because it is sometimes not a verbal noun."},
    {"type": "pair",
     "ar": "وحينئذ إما أن يدل على الحدث نحو: الويل، أو لا يدل عليه، لكن يصدق عليه نحو: «ضربته أنواعا، ورأيته ألفا».",
     "en": "In that case it either signifies the event, as with “al-wayl,” or it does not signify it but is true of it, as in “I beat him [in] kinds” (ḍarabtuhu anwāʿan) and “I saw him a thousand [times]” (raʾaytuhu alfan)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: أن الفعل الاصطلاحي المذكور أعم.",
     "en": "He means that the mentioned verb, in the technical sense, is more general."},
    {"type": "pair",
     "ar": "وذلك التعميم إما باعتبار كونه مذكورا وهو ظاهر، أو باعتبار كونه فعلا كما أفاد بقوله: أو إسما معطوفا على قوله: مقدرا،",
     "en": "That generalization is either with respect to its being mentioned, which is evident, or with respect to its being a verb, as he indicated by his words “or a noun,” coordinated with his words “supplied”;"},
    {"type": "pair",
     "ar": "فالفعل المذكور حكما يشمل المقدر، والاسم الذي فيه معنى الفعل.",
     "en": "so the verb mentioned by assimilated status covers the supplied [verb] and the noun containing the meaning of the verb."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة محمد:٤.",
     "en": "Qurʾān, Sūrat Muḥammad 47:4."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "عطف على قوله: «مذكورا» أولا،",
     "en": "Coordinated with his first [occurrence of] “mentioned”;"},
    {"type": "pair",
     "ar": "يعني: الفعل المذكور يشمل الملفوظ والمقدر والاسم؛ لأن المراد أعم من الفعل وشبهه، كما هو الشائع.",
     "en": "he means: the mentioned verb covers the uttered, the supplied and the noun; because what is meant is more general than the verb and what resembles it, as is common usage."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: احترازية خرج بها نحو: كرهت قيامي، كما ستعرفه.",
     "en": "That is: a restrictive [adjective], by which such as “I disliked my standing” (karihtu qiyāmī) is excluded, as you will come to know."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لم يرد اشتمال مفهوم الفعل على مفهوم الاسم، وإلا لخرج مثل: «جلست جلسة وضربت شيئا» إذا كني به عن الضرب،",
     "en": "He did not intend the containment of the concept of the verb upon the concept of the noun; otherwise such as “I sat a sitting” (jalastu jalsatan) and “I struck something” (ḍarabtu shayʾan), when it is used as a metonym for the beating, would be excluded."},
    {"type": "pair",
     "ar": "بل أراد أن تحقق الفعل باعتبار جزئه الذي هو المنسوب تحقق مدلول الاسم، وذكر من حيث إنه بيان للجزء ومتحد معه.",
     "en": "Rather, he intended that the realization of the verb, with respect to its part that is attributed [to the agent], is the realization of what the noun signifies, and [the noun] is mentioned inasmuch as it explicates the part and is one with it."},
    {"type": "pair",
     "ar": "ولا يخفى حينئذ دخول المثالين، وخروج «كرهت كراهتي»؛ لأن الكراهة التي هي مدلولة للفعل مغايرة للكراهة التي هي متعلقها في التحقق لتقدم وتأخر بينهما.",
     "en": "It is then not hidden that the two examples are included and that “I disliked my dislike” (karihtu karāhatī) is excluded; because the dislike signified by the verb differs in realization from the dislike that is its object, owing to the priority and posteriority between them."},
    {"type": "pair",
     "ar": "وكذا يخرج «ضربته تأديبا»؛ لأن الضرب وإن كان هو التأديب بحسب التحقق لكن لم يذكر التأديب من حيث إنه الضرب بل ذكر من حيث إنه علة له.",
     "en": "Likewise “I beat him for discipline” (ḍarabtuhu taʾdīban) is excluded; because the beating, even if it is the discipline in terms of realization, the discipline was not mentioned inasmuch as it is the beating, but inasmuch as it is its cause."},
    {"type": "pair",
     "ar": "لا يقال: قيد الاتحاد أيضا يخرج «كرهت كراهتي»، فلا حاجة في إخراجه اعتبار القيد السابق؛",
     "en": "It should not be said: the qualification of identity (ittiḥād) also excludes “karihtu karāhatī,” so there is no need, in excluding it, to take the preceding qualification into account;"},
    {"type": "pair",
     "ar": "لأنا نقول: قيد الاتحاد من تتمة السابق وتوابعه، فلا معنى لاعتبار بدون اعتبار أصله.",
     "en": "for we say: the qualification of identity is part of the completion of the preceding [qualification] and among its appendages, so there is no sense in considering it without considering its basis."},
]
