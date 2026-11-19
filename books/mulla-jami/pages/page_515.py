# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 515 (printed ٥١٤)."""

PAGE_NUMBER = 515
PRINTED_PAGE = "٥١٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «والتعليق إبطال العمل في» at the foot of PDF p. 514 (mid-sentence).
    {"type": "matn",
     "ar": "اللفظ لا في المعنى.",
     "en": "…wording, not in meaning."},
    {"type": "matn",
     "ar": "(ومنها) أي: ومن خصائص أفعال القلوب (أنه يجوز أن يكون فاعلها) أي: فاعل أفعال القلوب (ومفعولها ضميرين[[١]] متصلين لشيء واحد)",
     "en": "(And among them), that is, among the properties of the verbs of the heart (afʿāl al-qulūb), (is that their agent), that is, the agent of the verbs of the heart, (and their object may be two attached pronouns [referring] to one and the same thing)."},
    {"type": "matn",
     "ar": "وإنما قلنا: «متصلين»؛ لأنه إذا كان أحدهما منفصلا لم يختص جوازا اجتماعهما بفعل دون الآخر نحو: «إياك ظلمت»",
     "en": "We said “attached” only because, when one of them is detached, the permissibility of their combining is not peculiar to one verb as against another, as in “iyyāka ẓalamta” (it is yourself that you wronged)."},
    {"type": "matn",
     "ar": "(مثل: «علمتني منطلقا») و«علمتك منطلقا»، ولا يجوز ذلك في سائر الأفعال،",
     "en": "(As in “ʿalimtunī munṭaliqan” (I knew myself to be departing)) and “ʿalimtaka munṭaliqan” (you knew yourself to be departing). This is not permissible with the other verbs;"},
    {"type": "matn",
     "ar": "فلا يقال: «ضربتني وشتمتني»، بل يقال: «ضربت نفسي، وشتمت نفسي»،",
     "en": "so one does not say “ḍarabtunī wa-shatamtunī” (I struck me and reviled me); rather one says “ḍarabtu nafsī, wa-shatamtu nafsī” (I struck myself and reviled myself)."},
    {"type": "matn",
     "ar": "وذلك لأن أصل الفاعل أن يكون مؤثرا، والمفعول به متأثرا[[٢]]، وأصل المؤثر أن يغاير المتأثر،",
     "en": "That is because the agent in principle is the one exerting influence, and the direct object (mafʿūl bihi) the one receiving it; and in principle what exerts influence is other than what receives it."},
    # REVIEW: printed «بقدر الامكان» here without hamza, while the same phrase is printed «الإمكان» elsewhere on this page; transcribed as printed.
    {"type": "matn",
     "ar": "فإن اتحدا معنى كره اتفاقهما لفظا، فقصد -مع اتحادهما معنى- تغايرهما لفظا بقدر الامكان،",
     "en": "So if they are one in meaning, their being alike in wording is disliked, and what is sought — while they are one in meaning — is their being different in wording as far as possible."},
    {"type": "matn",
     "ar": "فمن ثمة قالوا: «ضربت نفسي» ولم يقولوا: «ضربتني»،",
     "en": "Hence they said “ḍarabtu nafsī” (I struck myself) and did not say “ḍarabtunī”;"},
    {"type": "matn",
     "ar": "فإن الفاعل والمفعول فيه ليسا بمتغايرين بقدر الإمكان؛ لاتفاقهما من حيث[[٣]] كون كل واحد منهما ضميرا متصلا،",
     "en": "for the agent and the object in it are not different as far as possible, since they agree in respect of each of them being an attached pronoun;"},
    {"type": "matn",
     "ar": "بخلاف: «ضربت نفسي»، فإن النفس بإضافتها إلى ضمير المتكلم صار كأنها غيره؛ لغلبة مغايرة المضاف للمضاف إليه، فصار الفاعل والمفعول فيه متغايرين بقدر الإمكان.",
     "en": "unlike “ḍarabtu nafsī”: for “nafs” (self), by its annexation to the pronoun of the speaker, has become as though it were other than him, because the annexed term is predominantly other than that to which it is annexed; so the agent and the object in it have become different as far as possible."},
    {"type": "matn",
     "ar": "وأما أفعال القلوب فإن المفعول به فيها ليس المنصوب الأول في الحقيقة، بل مضمون الجملة،",
     "en": "As for the verbs of the heart, the direct object in them is not in reality the first accusative, but the content of the sentence;"},
    {"type": "matn",
     "ar": "فجاز اتفاقهما لفظا؛ لأنهما ليسا في الحقيقة فاعلا ومفعولا به،",
     "en": "so their being alike in wording is permissible, since they are not in reality agent and direct object."},
    {"type": "matn",
     "ar": "ومما أجري مجرى أفعال القلوب: «فقدتني، وعدمتني»؛ لأنهما نقيضا «وجدتني»[[٤]]، فحملا عليه حمل النقيض على النقيض،",
     "en": "Among what is treated like the verbs of the heart are “faqadtunī” (I lost myself) and “ʿadimtunī” (I was bereft of myself), since they are the contraries of “wajadtunī” (I found myself); so they are assimilated to it, as a contrary is assimilated to its contrary."},
    {"type": "matn",
     "ar": "وكذلك أجري رأي البصرية[[٥]] والحلمية[[٦]] على رأي القلبية،",
     "en": "Likewise raʾā of sight and raʾā of dreaming are treated like raʾā of the heart [i.e., of cognition],"},
    {"type": "matn",
     "ar": "فجوز فيهما ما جوز فيه من كون فاعلهما ومفعولهما ضميرين لشيء واحد، كقول الشاعر:",
     "en": "and what is permitted in it is permitted in them, namely that their agent and their object be two pronouns for one and the same thing, as in the poet’s saying:…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أما إن كان أحدهما ضميرا متصلا والآخر ظاهرا نحو: زيد أظن قائما، وأظنه زيد قائما لم يجز المثال الأول مطلقا، وجاز الثاني في أفعال القلوب خاصة،",
     "en": "If one of them is an attached pronoun and the other an overt noun, as in “zaydun aẓunnu qāʾiman” and “aẓunnuhu zaydun qāʾiman”, the first example is not permissible at all, and the second is permissible with the verbs of the heart only;"},
    {"type": "pair",
     "ar": "وإن كان الضمير منفصلا جائز مطلقا، كذا في الرضي.",
     "en": "and if the pronoun is detached, it is permissible without restriction. So [it is] in al-Raḍī."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "من قبيل العطف على معمولي عاملين، والمجرور مقدم.",
     "en": "This is of the type of coordination upon the governed terms of two governing words, the genitive being placed first."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إن اختلفا من حيث كون أحدهما مرفوعا والآخر منصوبا، فإن الواجب رعاية تغايرهما بقدر الإمكان.",
     "en": "Even if they differ in respect of one of them being nominative and the other accusative; for what is required is to observe their difference as far as possible."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: في أصل الوضع، فإن «وجد» بمعنى «أصاب»، ثم استعمل بمعنى علم.",
     "en": "That is, in the original assignment; for “wajada” means “aṣāba” (to come upon), and it was then used in the sense of “ʿalima” (to know)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: رأى بمعنى أبصر، والحلمية الحلم هو النوم.",
     "en": "That is, raʾā in the sense of abṣara (to see); and al-ḥulmiyya [is from] al-ḥulm, which is sleep."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: أجرى التي بمعنى «أبصر»، والتي بمعنى رأى في المنام مجرى «رأى» التي بمعنى علم للتشارك اللفظي،",
     "en": "That is, he treated the one meaning “abṣara” and the one meaning “he saw in a dream” like the “raʾā” that means “ʿalima”, because of the shared wording;"},
    {"type": "pair",
     "ar": "وإن كان منصوبا يتعلق الفعل به حقيقة.",
     "en": "even if it is an accusative to which the verb is connected in reality."},
    {"type": "pair",
     "ar": "في القاموس: الحلم بالضم وبضمتين: الرؤيا.",
     "en": "In al-Qāmūs: al-ḥulm, with a ḍamma and with two ḍammas [ḥulum], is a dream (al-ruʾyā)."},
]
