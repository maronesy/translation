# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 465 (printed ٤٦٤)."""

PAGE_NUMBER = 465
PRINTED_PAGE = "٤٦٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… يلزم تعدد» at the foot of PDF p. 464 (mid-sentence).
    {"type": "matn",
     "ar": "الفاعل (فهي) أي: تلك الصفة حينئذ (كالفعل)",
     "en": "…of agents. (So it), that is, that adjective in that case, (is like the verb):"},
    {"type": "matn",
     "ar": "فكما أن الفعل لا يثنى ولا يجمع بتثنية فاعله الظاهر وجمعه، كذلك تلك الصفة لا تثنى ولا تجمع بتثنية معمولها وجمعه",
     "en": "just as the verb is not put in the dual or plural when its overt agent is dual or plural, so that adjective is not put in the dual or plural when its governed term is dual or plural."},
    {"type": "matn",
     "ar": "(وإلا) أي: وإن لم ترفع معمول الصفة بها، بل تنصب أو تجر (ففيها ضمير الموصوف) ليكون فاعلا لها",
     "en": "(Otherwise), that is, if you do not put the governed term of the adjective in the nominative by it, but in the accusative or genitive, (then there is in it a pronoun of the qualified noun), to be its agent;"},
    {"type": "matn",
     "ar": "(فتؤنث) أي: أنث الصفة بتأنيث الموصوف، فتقول: «هند حسنة وجه أو حسنة وجها»",
     "en": "(so it is made feminine), that is, make the adjective feminine when the qualified noun is feminine, and you say: “Hindun ḥasanatu wajhin” or “ḥasanatun wajhan” (Hind is fair of face);"},
    {"type": "matn",
     "ar": "(وتثنى) أي: الصفة إذا كان الموصوف تثنية مثل: «الزيدان حسنا وجه، أو حسنان وجها»",
     "en": "(and it is put in the dual), that is, the adjective, when the qualified noun is a dual, as in “al-Zaydāni ḥasanā wajhin” or “ḥasanāni wajhan”;"},
    {"type": "matn",
     "ar": "(وتجمع) أيضا الصفة إذا كان الموصوف جمعا مثل: «الزيدون حسنو وجه وحسنون وجها».",
     "en": "(and it is put in the plural), the adjective likewise, when the qualified noun is a plural, as in “al-Zaydūna ḥasanū wajhin” and “ḥasanūna wajhan”."},
    {"type": "matn",
     "ar": "(اسما الفاعل والمفعول غير المتعديين) أي: اسم الفاعل الغير المتعدي إلى مفعول، واسم المفعول الغير المتعدي أيضا إلى مفعول؛",
     "en": "(The active and passive participles that are not transitive), that is, the active participle not transitive to an object, and the passive participle likewise not transitive to an object,"},
    {"type": "matn",
     "ar": "لاشتقاقه من الفعل المتعدي إلى مفعول واحد، فإذا بني اسم المفعول منه أقيم ذلك المفعول مقام الفاعل، فبقي غير متعد إلى مفعول",
     "en": "since it is derived from the verb transitive to one object; when the passive participle is formed from it, that object is put in the place of the agent, and it remains not transitive to an object,"},
    {"type": "matn",
     "ar": "(مثل الصفة[[١]] المشبهة في ذلك) أي: فيما ذكر من الأقسام الثمانية عشر،",
     "en": "(are like the resembling adjective (al-ṣifa al-mushabbaha) in that), that is, in what was mentioned of the eighteen cases:"},
    {"type": "matn",
     "ar": "فيرفعان الفاعل ومفعول ما لم يسم فاعله، وينصبانهما، ويضافان إليهما، تقول: «زيد قائم الأب ومضروب الأب» برفع الأب ونصبه وجره.",
     "en": "they put the agent and the object of the verb whose agent is unnamed in the nominative, in the accusative, and are annexed to them; you say “Zaydun qāʾimu l-ab” (Zayd is standing of father) and “maḍrūbu l-ab” (beaten of father), with “al-ab” in the nominative, accusative and genitive."},
    {"type": "matn",
     "ar": "وإذا كانا متعديين لا يجوز إضافتهما إليهما، ولا نصبهما لئلا يلزم الالتباس بالمفعول،",
     "en": "When they are transitive, neither their annexation to them nor their putting them in the accusative is permitted, lest confusion with the object follow."},
    {"type": "matn",
     "ar": "فإذا قلنا مثلا: «زيد ضارب أباه، وزيد معط أباه» لم يعلم أن «أباه» في المثال الأول مفعول الضارب أو فاعل له، نصب تشبيها بالمفعول،",
     "en": "If we say, for example, “Zaydun ḍāribun abāhu” and “Zaydun muʿṭin abāhu”, it would not be known whether “abāhu” in the first example is the object of “ḍārib” or its agent put in the accusative by resemblance to the object;"},
    {"type": "matn",
     "ar": "وفي المثال الثاني أنه مفعول ثان لمعط، أو مفعول أول أقيم مقام الفاعل، ونصب تشبيها بالمفعول، والمفعول الثاني محذوف.",
     "en": "and in the second example, whether it is the second object of “muʿṭin”, or a first object put in the place of the agent and put in the accusative by resemblance to the object, the second object being omitted."},
    {"type": "matn",
     "ar": "(وكذلك) مثل الصفة المشبهة (المنسوب[[٢]]) تقول: «زيد تميمي الأب» مرفوعا، ومنصوبا، ومجرورا.",
     "en": "(And likewise), like the resembling adjective, is (the relative adjective (al-mansūb)); you say “Zaydun tamīmiyyu l-ab” (Zayd is Tamīmī of father), in the nominative, accusative and genitive."},

    {"type": "section", "ar": "[اسم التفضيل]",
     "en": "The Elative (Ism al-Tafḍīl)"},

    {"type": "matn",
     "ar": "(اسم التفضيل: ما اشتق) أي: اسم اشتق (من فعل) أي: حدث[[٣]] (لموصوف) قام به الفعل[[٤]] أو وقع عليه،",
     "en": "(The elative (ism al-tafḍīl) is what is derived), that is, a noun derived (from a verb), that is, an event, (for a qualified thing) in which the action subsists or on which it falls;"},
    {"type": "matn",
     "ar": "والتعميم لقصد شمول قسمي اسم التفضيل، أعني: ما",
     "en": "the generalization is intended to include both kinds of elative, namely, what…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيما ذكر من رفع المعمول ونصبه وجره من غير اشتراط زمان الحال أو الاستقبال.",
     "en": "In what was mentioned of putting the governed term in the nominative, accusative and genitive, without the condition of present or future time."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وغير المنسوب أيضا من الأسماء الجامدة التي أجريت مجرى الصفات المشبهة نحو: هو شمس الوجه أي: حسن الوجه وهو قليل.",
     "en": "Likewise other than the relative adjective, among the non-derived nouns treated like resembling adjectives, as in “huwa shamsu l-wajhi” (he is sun of face), that is, fair of face; and this is rare."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: دل على حدث بإقامة المدلول مقام الدال، وهو المصدر،",
     "en": "That is, [what] signifies an event, the signified being put in place of the signifier, which is the maṣdar;"},
    {"type": "pair",
     "ar": "ولم يفسره بالفعل المصطلح؛ لأن الاشتقاق من المصدر عند البصريين، ولرعاية المطابقة بما سبق.",
     "en": "he did not explain it as the verb in the technical sense, because derivation is from the maṣdar according to the Baṣrans, and to keep agreement with what preceded."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: اختار \"الموصوف\" على \"لمن قام\"، أو لمن وقع قصد التعميم، والتعميم شموله للقسمين.",
     "en": "He means: he chose “qualified thing” over “for one in whom [it] subsists” or “for one on whom [it] falls” to intend generality, the generality being its covering both kinds."},
]
