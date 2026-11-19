# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 246 (printed ٢٤٥)."""

PAGE_NUMBER = 246
PRINTED_PAGE = "٢٤٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ونحو: «شهدت الحرب» from the foot of PDF p. 245.
    {"type": "matn",
     "ar": "إيقاعا للصلح[[١]] بين الفريقين»، فإن زمان المفعول له أعني: إيقاع الصلح بعض زمان الفعل أعني: شهود الحرب.",
     "en": "…to bring about peace between the two parties,” for the time of the object of purpose, namely bringing about peace, is part of the time of the action, namely witnessing the war."},
    {"type": "matn",
     "ar": "واحترز بذلك القيد عما إذا لم يكن مقارنا له في الوجود، نحو: «أكرمتك اليوم لوعدي بذلك أمس».",
     "en": "By that restriction he guarded against its not being concurrent with it in existence, as in “I honoured you today because of my promising it yesterday.”"},
    {"type": "matn",
     "ar": "وإنما اشترط هذه الشرائط؛ لأنه بهذه الشرائط[[٢]] يشبه المصدر، فيتعلق بالفعل بلا واسطة تعلق المصدر به، بخلاف ما إذا اختل شيء منها.",
     "en": "He stipulated these conditions only because with them it resembles the maṣdar, and so attaches to the verb without an intermediary, as the maṣdar attaches to it; unlike when any of them is lacking."},

    {"type": "section", "ar": "[المفعول معه]",
     "en": "The Object of Accompaniment (al-Mafʿūl maʿahu)"},

    {"type": "matn",
     "ar": "(المفعول معه) أي: الذي فعل بمصاحبته بأن يكون الفاعل مصاحبا له في صدور الفعل عنه، أو المفعول في وقوع الفعل عليه.",
     "en": "(The object of accompaniment (al-mafʿūl maʿahu)), that is, that in whose company an action is done, in that the agent accompanies it in the action’s issuing from him, or the object [accompanies it] in the action’s falling upon it."},
    {"type": "matn",
     "ar": "فقوله: «معه» مفعول ما لم يسم فاعله أسند إليه المفعول كما أسند إلى الجار والمجرور في المفعول به، وفيه، وله، والضمير المجرور راجع إلى اللام.",
     "en": "His word “maʿahu” is the subject of the passive (mafʿūl mā lam yusamma fāʿiluhu), the participle “mafʿūl” being predicated of it, just as it is predicated of the preposition and its genitive in mafʿūl bihi, fīhi and lahu; and the genitive pronoun refers back to the lām [the definite article, al-mafʿūl]."},
    {"type": "matn",
     "ar": "واعتذر عن نصبه بما جوزه بعض النحاة من إسناد الفعل إلى لازم النصب، وتركه منصوبا جريا على ما هو عليه في الأكثر،",
     "en": "He excused its being in the accusative by what some grammarians allowed: predicating the verb of what is necessarily accusative, and leaving it in the accusative, following what it mostly is;"},
    {"type": "matn",
     "ar": "وإليه ذهب في قوله تعالى: ﴿لقد تقطع بينكم﴾[[٣]] على قراءة النصب، وفي بعض الحواشي: أن هذا الرأي شريف جدا[[٤]].",
     "en": "and this is the view taken of His words, the Exalted: “Surely [the bond] between you has been severed” on the reading with the accusative. In one of the glosses [it is said] that this view is very fine."},
    {"type": "matn",
     "ar": "وقيل: الوجه أن يجعل من قبيل:",
     "en": "It has been said: the right way is to treat it as being of the type of:"},
    {"type": "verse",
     "ar": "............          وقد حيل بين العير والنزوان[[٥]]",
     "en": "“… and the wild ass was barred from leaping.”"},
    {"type": "matn",
     "ar": "فإن مفعول ما لم يسم فاعله فيه الضمير الراجع إلى مصدره، أي: حيل الحيلولة؛ لأن «بين» للزوم ظرفيته لا يقام مقام الفاعل،",
     "en": "For the subject of the passive in it is the pronoun referring back to its maṣdar, that is, “the barring was barred”; because “bayna,” being necessarily adverbial, is not made to stand in place of the agent."},
    {"type": "matn",
     "ar": "فعلى هذا معناه: الذي فعل فعل بمصاحبته على أن يكون مفعول ما لم يسم فاعله ضميرا راجعا إلى مصدره، والضمير المجرور للموصول.",
     "en": "On this view its meaning is: “that in whose company a doing is done,” the subject of the passive being a pronoun referring back to its maṣdar, and the genitive pronoun [referring] to the relative."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا يخفى أنه يصح هذا التركيب وإن لم يوقع الشاهد الصلح،",
     "en": "It is not hidden that this construction is correct even if the one witnessing did not bring about peace;"},
    # REVIEW: «فبالوجود» printed; sense unclear (perhaps for «فبالأولى»); transcribed as printed.
    {"type": "pair",
     "ar": "فلم يجب كونه مقارنا له في الوجود إذا لم يجب الوجود فضلا عن المقارنة، فبالوجود",
     "en": "so its being concurrent with it in existence is not required, since existence is not required, let alone concurrence; so by existence…"},
    {"type": "pair",
     "ar": "إلا أن يقال: المراد بالمقارنة هنا أعم من المقارنة في الوجود في الواقع، أو في قصد الفاعل.",
     "en": "Unless it is said: concurrence here means something more general: concurrence in existence in reality, or in the agent’s intention."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال المصنف: إنما اشترط ذلك؛ لأن علة الأفعال كثيرا ما تجيء جامعة للشرائط، فحصولها دليل على اللام المقدرة.",
     "en": "The author said: this was stipulated only because the reasons for actions often come fulfilling the conditions, so their presence is evidence of the implied lām."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة الأنعام: ٩٤.",
     "en": "Qurʾān, Sūrat al-Anʿām 6:94."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لجعل ما هو محط الفائدة قائما مقام الفاعل، ولخلوه عن تكلف اعتبار ضمير راجع إلى مصدر الفعل، عن جعل المصدر نائبا مناب الفاعل من غير تخصيص.",
     "en": "Because it makes what is the focus of the information stand in place of the agent, and because it is free from the strain of positing a pronoun referring back to the verb’s maṣdar, [and] from making the maṣdar stand in for the agent without specification."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قال قدس سره في الحاشية: العير الحمار الوحشي والأهلي. والنزوان: الوثوب.",
     "en": "He said, may his secret be sanctified, in the gloss: al-ʿayr is the wild and the domestic ass; and al-nazawān is leaping."},
]
