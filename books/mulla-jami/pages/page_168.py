# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 168 (printed ١٦٧)."""

PAGE_NUMBER = 168
PRINTED_PAGE = "١٦٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "ونظر بعض النحاة[[١]] إلى صورة التعدد وجوز العطف،",
     "en": "Some grammarians considered the form of the multiplicity and permitted conjunction."},
    {"type": "matn",
     "ar": "ولا يبعد أن يقال: مراد المصنف بتعدد الخبر ما يكون بغير عاطف؛ لأنه التعدد بالعاطف لا خفاء فيه[[٢]]، ولا في الخبر ولا في المبتدأ ولا في غيرهما،",
     "en": "It is not far-fetched to say that what the author means by the multiplicity of the khabar is that which is without a conjunctive particle; because multiplicity with a conjunctive particle involves no obscurity—neither in the khabar, nor in the mubtadaʾ, nor in anything else;"},
    {"type": "matn",
     "ar": "وأيضا المتعدد بالعطف ليس بخبر بل هو من توابعه[[٣]]، ولهذا أورد في المثال الخبر المتعدد بغير عاطف، ولو جعل التعدد أعم، فالاقتصار عليه لذلك.",
     "en": "moreover, what is multiplied by conjunction is not a khabar but one of its appositives (tawābiʿ). For this reason he gave as the example a khabar multiplied without a conjunctive particle; and even if he made multiplicity more general, the restriction to it is for that reason."},

    {"type": "section", "ar": "[ دخول الفاء في خبر المبتدأ ]",
     "en": "The Entry of the Fāʾ into the Khabar of the Mubtadaʾ"},

    {"type": "matn",
     "ar": "(وقد يتضمن المبتدأ معنى الشرط[[٤]]) وهو سببية الأول للثاني[[٥]] أو للحكم به[[٦]]، فلا يرد عليه[[٧]] نحو: ﴿وما بكم من نعمة فمن الله﴾[[٨]]،",
     "en": "“The mubtadaʾ may implicitly contain the meaning of the condition (sharṭ),” namely the first's being the cause of the second, or of the judgement [made] by it; so the like of “Whatever blessing you have is from Allah” does not count against it;"},
    {"type": "matn",
     "ar": "فيشبه المبتدأ الشرط[[٩]] في سببيته للخبر سببية الشرط للجزاء.",
     "en": "so the mubtadaʾ resembles the condition in its being the cause of the khabar, as the condition is the cause of the apodosis (jazāʾ)."},
    {"type": "matn",
     "ar": "(فيصح دخول الفاء في الخبر) ويصح عدم دخوله فيه[[١٠]]، نظرا إلى مجرد تضمن المبتدأ معنى الشرط.",
     "en": "“So the entry of the fāʾ into the khabar is valid,” and its non-entry into it is valid, considering merely the mubtadaʾ's implicitly containing the meaning of the condition."},
    {"type": "matn",
     "ar": "وأما إذا قصد الدلالة على ذلك المعنى في اللفظ، فيجب دخول",
     "en": "But when indicating that meaning in the wording is intended, the entry of…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وهو أبو علي الفارسي، وتبعه الرضي.",
     "en": "He is Abū ʿAlī al-Fārisī, and al-Raḍī followed him."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: في جوازه، ففي تمثيل المصنف إظهار لما خفي وإعراض عما ظهر.",
     "en": "That is: in its permissibility. So in the author's choice of example there is a making manifest of what was obscure and a turning away from what was evident."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إلا أن المعطوف على الخبر في حكمه.",
     "en": "Except that what is conjoined to the khabar takes its ruling."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الإضافة بيانية أو لامية.",
     "en": "The genitive construction [maʿnā al-sharṭ] is explicative (bayāniyya) or of the lām type (lāmiyya)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: ليس معنى الشرط سببية الأول للثاني، بل لزوم الثاني للأول، كما في جميع الشرط والجزاء،",
     "en": "Shaykh al-Raḍī said: the meaning of the condition is not the first's being the cause of the second, but the second's being entailed by the first, as with every condition and apodosis;"},
    {"type": "pair",
     "ar": "فلا يرد نحو قوله تعالى: ﴿وما بكم من نعمة فمن الله﴾ (سورة النحل: ٥٣)،",
     "en": "so the like of His words, the Exalted, “Whatever blessing you have is from Allah” (Qurʾān, Sūrat al-Naḥl 16:53) does not count against it;"},
    {"type": "pair",
     "ar": "لكن الشارح فسره بما يوافق كلام المتن في بحث كلم المجازاة.",
     "en": "but the commentator explained it in a way that accords with the wording of the base text in the discussion of the words of conditional requital (kalim al-mujāzāt)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فإن الجمل الجزائية كثيرا ما تورد ولا يراد مضمونها، بل يراد الإخبار بها.",
     "en": "For apodotic sentences are often adduced without their content being meant; rather, informing by them is meant."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: على هذا الأصل هذا المثال، أي: خروجه، فلا يكون الأصل جامعا،",
     "en": "That is: against this principle [does not count] this example, that is, its falling outside it, so that the principle would not be comprehensive;"},
    {"type": "pair",
     "ar": "ولم يدفع بالحكم بشذوذه لكثرته،",
     "en": "and it was not answered by ruling it anomalous, because of its frequency."},
    {"type": "pair",
     "ar": "وتوجيه الورود على ما قالوا: إن كون النعمة معهم ليس سببا لكونه من الله.",
     "en": "The objection is explained, according to what they said, thus: the blessing's being with them is not the cause of its being from Allah."},
    {"type": "pair",
     "ar": "ولو قيل: بتعليل أفعاله تعالى بالغرض لكان سبيلا إلى ظهور تضمنه معنى الشرط،",
     "en": "Were it held that His acts, the Exalted, are explained by a purpose (gharaḍ), that would be a way to make evident its implicitly containing the meaning of the condition;"},
    {"type": "pair",
     "ar": "فوقوع الزمخشري في هذه الإشكال غفلة عن سهولة حال العاقل على قاعدة الاعتزال.",
     "en": "so al-Zamakhsharī's falling into this difficulty is an oversight of how easy the matter is for the reasoner on the principle of the Muʿtazila."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "سورة النحل: ٥٣.",
     "en": "Qurʾān, Sūrat al-Naḥl 16:53."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "لما كان المبتدأ دخيلا في هذا المعنى خالف الشرط في جواز ترك الفاء في خبره،",
     "en": "Since the mubtadaʾ is an intruder in this meaning, it differs from the condition in the permissibility of omitting the fāʾ in its khabar,"},
    {"type": "pair",
     "ar": "وفي جواز كون الصلة أو الصفة ماضية أريد بها المضي لكنه قليل، وفي جواز كون الظرف صلة أو صفة له.",
     "en": "in the permissibility of the relative clause or the adjective being a past [verb] meant as past—though this is rare—and in the permissibility of an adverbial phrase (ẓarf) being its relative clause or adjective."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "لإفادة المبتدأ والخبر فائدة تامة غير السببية، فلا حاجة إلى الفاء. وأما عند قصد السببية، فلا بد من الفاء لإفادته.",
     "en": "Because the mubtadaʾ and khabar convey a complete meaning other than causation, so there is no need for the fāʾ. But when causation is intended, the fāʾ is indispensable to convey it."},
    {"type": "pair",
     "ar": "وأما عند عدم قصد السببية، فلا حاجة إلى الفاء، فذكره يكون لغوا فيجب تركه،",
     "en": "And when causation is not intended, there is no need for the fāʾ, so mentioning it would be redundant and its omission is required."},
    {"type": "pair",
     "ar": "وفيه أن الاحتمال عند استعمال هذا المبتدأ في التراكيب منحصر في قصد السببية وعدمه، ففي الاستعمال إيراد الفاء أو تركه واجب،",
     "en": "Against this: when this mubtadaʾ is used in constructions, the possibilities are restricted to causation being intended or not; so in usage, either including the fāʾ or omitting it is obligatory;"},
    {"type": "pair",
     "ar": "فصحة دخول الفاء الخالي من الوجوب والامتناع كما ذكره الشارح لم يكن في استعماله.",
     "en": "so a validity of the fāʾ's entry free of both obligation and prohibition, as the commentator mentioned, does not occur in its usage."},
]
