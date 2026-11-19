# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 374 (printed ٣٧٣)."""

PAGE_NUMBER = 374
PRINTED_PAGE = "٣٧٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «مثاله:» at the foot of PDF p. 373 (the verse is the example).
    {"type": "verse",
     "ar": "إن من يدخل الكنيسة يوما      يلق فيها جاذرا وظباء",
     "en": "…“Indeed, whoever enters the church one day / will meet in it wild-cow calves and gazelles.”"},
    {"type": "matn",
     "ar": "(إلا مع «أن») المفتوحة (إذا خففت، فإنه) أي: حذفه بنية الإضمار ههنا مع كونه منصوبا[[١]] (لازم)",
     "en": "(Except with “an”) — the one with fatḥa — (when it is lightened, for it), that is, its omission with the pronoun intended, here, although it is accusative, (is obligatory),"},
    {"type": "matn",
     "ar": "كقوله تعالى: «وآخر دعواهم أن الحمد لله رب العالمين»[[٢]]",
     "en": "as in the words of the Exalted: “and the last of their call is: Praise be to Allah, Lord of the worlds”."},
    {"type": "matn",
     "ar": "وذلك لأنه قد خفف «إن وأن» لثقلهما بالتشديد الواقع فيهما،",
     "en": "That is because “inna” and “anna” have been lightened on account of their heaviness through the doubling that occurs in them;"},
    {"type": "matn",
     "ar": "وبعد تخفيفهما وجدوا «إن» المكسورة المخففة عاملة في الملفوظ، كما قال الله تعالى: «وإن كلا لما ليوفينهم»[[٣]]",
     "en": "and after their lightening they found the lightened “in” with kasra governing an expressed word, as Allah the Exalted said: “And indeed, to each of them your Lord will fully repay”,"},
    {"type": "matn",
     "ar": "ولم يجدوا أن المفتوحة المخففة عاملة في الملفوظ، مع أن «أن» المفتوحة أقوى شبها بالفعل من المكسورة فهي أجدر بالعمل،",
     "en": "but they did not find the lightened “an” with fatḥa governing an expressed word, although “an” with fatḥa bears a stronger resemblance to the verb than the one with kasra, and so is more deserving of government."},
    {"type": "matn",
     "ar": "فإذا لم يجدوها عاملة في الملفوظ قدروا عملها في ضمير الشأن؛ لئلا يزيد المكسورة عليها عملا، مع أنه أجدر به،",
     "en": "So, since they did not find it governing an expressed word, they supposed its government to be in the pronoun of the matter, lest the one with kasra exceed it in government, although it is more deserving of it."},
    {"type": "matn",
     "ar": "ولم يجوزوا إظهار ذلك الضمير، لئلا يفوت التخفيف المطلوب ههنا، كما يدل عليه حذف النون، وحكموا بلزوم حذف ضمير الشأن مع «أن» المفتوحة إذا خففت.",
     "en": "They did not permit that pronoun to be expressed, lest the lightening sought here be lost, as the omission of the nūn indicates; and they ruled that the pronoun of the matter must be omitted with “an” with fatḥa when it is lightened."},

    {"type": "section", "ar": "[أسماء الإشارة]",
     "en": "Demonstrative Nouns"},

    {"type": "matn",
     "ar": "(أسماء الإشارة) أي: أسماء الإشارة المعدودة في المبنيات بحسب الاصطلاح",
     "en": "(Demonstrative nouns) (asmāʾ al-ishāra), that is, the demonstrative nouns counted among the indeclinables according to technical usage,"},
    {"type": "matn",
     "ar": "(ما وضع) أي: أسماء وضع كل واحد منها[[٤]] (لمشار إليه) أي: لمعنى مشار إليه إشارة حسية[[٥]] بالجوارح والأعضاء؛",
     "en": "(are what has been coined), that is, nouns each one of which has been coined, (for something pointed to), that is, for a meaning pointed to by a sensory pointing with the limbs and members,"},
    {"type": "matn",
     "ar": "لأن الإشارة عند إطلاقها حقيقة في الإشارة الحسية، فلا يرد الضمير الغائب[[٦]] وأمثاله، فإنها للإشارة إلى معانيها إشارة ذهنية لا حسية،",
     "en": "because “pointing”, when used without qualification, is literally sensory pointing. So the third-person pronoun and its like are not an objection, for they serve to point to their meanings by a mental, not a sensory, pointing…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فليس حذفه حذف ضمير مراد بلا دليل عليه؛ لأن التزام حذفه جعل حذفه جادة لأهل اللسان وطريقا واضحا.",
     "en": "So its omission is not the omission of an intended pronoun without any indication of it, because the consistent omission of it has made its omission a beaten road for the people of the language and a clear path."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة يونس: ١٠.",
     "en": "Qurʾān, Sūrat Yūnus 10:10."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة هود: ١١١.",
     "en": "Qurʾān, Sūrat Hūd 11:111."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إنما فسر بذلك؛ لأن المفسر بحسب الظاهر هو المجموع، ووضع المجموع وضع أجزائه.",
     "en": "He explained it thus only because what is explained is, on the face of it, the aggregate, and the coining of the aggregate is the coining of its parts."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هي تخييل امتداد واصل بين المخيل، وما يصير غاية لذلك الامتداد، وهي لا تكون إلا إلى محسوس مشاهد.",
     "en": "It is the imagining of an extension reaching between the one who imagines and what becomes the end-point of that extension; and it is directed only to something sensible and seen."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ولا يرد أيضا أن هذا تعريف للشيء بما يساويه في المعرفة والجهالة؛",
     "en": "Nor is there the objection that this defines a thing by what is equal to it in being known and unknown,"},
    {"type": "pair",
     "ar": "لأن المعرف ليس ما يفهم من الأسماء مفردة. وقد أضيف إلى الإشارة، بل لذلك المركب الإضافي معنى اصطلاحي كما أشار إليه",
     "en": "because what is defined is not what is understood from “nouns” taken singly and then annexed to “pointing”; rather, that annexation compound has a technical meaning, as he indicated,"},
    {"type": "pair",
     "ar": "أريد بيانه بالإشارة المعلومة لكل واحد،",
     "en": "which is meant to be explained by the pointing known to everyone."},
    {"type": "pair",
     "ar": "ومن الظاهر أيضا أنه ليس تعريفا للشيء بنفسه كما توهم؛ لأن المأخوذ في المعرف جزؤه، بل قيده. وإنما يكون كذلك لو كان نفسه مأخوذا فيه.",
     "en": "It is also evident that it is not a definition of a thing by itself, as has been imagined, because what is taken into the definition is its part — or rather its qualifier; it would be so only if the thing itself were taken into it."},
]
