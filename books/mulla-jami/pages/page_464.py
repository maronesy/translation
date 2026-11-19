# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 464 (printed ٤٦٣)."""

PAGE_NUMBER = 464
PRINTED_PAGE = "٤٦٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… أعني: حذف» at the foot of PDF p. 463 (mid-sentence).
    {"type": "matn",
     "ar": "التنوين، ولا يتعرض لأعظمهما مع إمكانه، وهو حذف الضمير مع الاستغناء عنه بما استكن في الصفة،",
     "en": "…the tanwīn (nunation), and not to undertake the greater of the two although it is possible, namely omitting the pronoun while dispensing with it through what is latent in the adjective;"},
    {"type": "matn",
     "ar": "والذي أجازها بلا قبح النظر إلى حصول شيء من التخفيف في الجملة، وهو حذف التنوين.",
     "en": "and what made it permissible without ugliness [for the Kūfans] is regard to the occurrence of some lightening on the whole, namely the omission of the tanwīn."},
    {"type": "matn",
     "ar": "(والبواقي) من الأقسام الثمانية عشر التي خرجت منها الأقسام الثلاثة المذكورة، وهي خمسة عشر قسما",
     "en": "(The remaining ones), of the eighteen cases from which the three cases mentioned have been excluded, and they are fifteen cases:"},
    {"type": "matn",
     "ar": "(ما كان فيه ضمير واحد منها) أي: من تلك البواقي:",
     "en": "(that among them in which there is one pronoun), that is, among those remaining ones:"},
    {"type": "matn",
     "ar": "إما في الصفة، وهو سبعة أقسام: «الحسن الوجه» بنصب المعمول، و«الحسن الوجه» بجره، و«حسن الوجه» بنصبه، و«حسن الوجه» بجره، و«الحسن وجها» و«حسن وجها» بنصبه، و«حسن وجه» بجره.",
     "en": "either in the adjective, and that is seven cases: “al-ḥasanu l-wajha” with the governed term in the accusative, “al-ḥasanu l-wajhi” with it in the genitive, “ḥasanun al-wajha” with it in the accusative, “ḥasanu l-wajhi” with it in the genitive, “al-ḥasanu wajhan” and “ḥasanun wajhan” with it in the accusative, and “ḥasanu wajhin” with it in the genitive;"},
    {"type": "matn",
     "ar": "وإما في المعمول مثل: «الحسن وجهه، وحسن وجهه» برفعه فيهما، وهما قسمان،",
     "en": "or in the governed term, as in “al-ḥasanu wajhuhu” and “ḥasanun wajhuhu”, with it in the nominative in both, and these are two cases."},
    {"type": "matn",
     "ar": "والمجموع تسعة (أحسن)؛ لأن الضمير فيه بقدر الحاجة من غير زيادة ولا نقصان.",
     "en": "The total, nine, (is best), because the pronoun in it is in the measure of need, without excess or deficiency."},
    {"type": "matn",
     "ar": "(وما فيه ضميران منها) أحدهما: في الصفة، والآخر في المعمول، مثل: «حسن وجهه، والحسن وجهه» بنصبه فيهما، فهو قسمان:",
     "en": "(That among them in which there are two pronouns), one of them in the adjective and the other in the governed term, as in “ḥasanun wajhahu” and “al-ḥasanu wajhahu”, with it in the accusative in both, and that is two cases,"},
    {"type": "matn",
     "ar": "(حسن) لاشتماله على الضمير المحتاج إليه، وغير أحسن لاشتمال على ضمير زائد[[١]] على قدر الحاجة.",
     "en": "(is good), because it contains the pronoun that is needed, but not best, because of containing a pronoun in excess of the measure of need."},
    {"type": "matn",
     "ar": "(وما لا ضمير فيه منها) وهو أربعة أقسام: «الحسن الوجه، وحسن الوجه، وحسن وجه، والحسن وجه» برفعه فيها",
     "en": "(That among them in which there is no pronoun), and that is four cases, “al-ḥasanu l-wajhu”, “ḥasanun al-wajhu”, “ḥasanun wajhun” and “al-ḥasanu wajhun”, with it in the nominative in them,"},
    {"type": "matn",
     "ar": "(قبيح) لعدم الرابطة[[٢]] بالموصوف لفظا.",
     "en": "(is ugly), because of the absence of an explicit link to the qualified noun."},
    {"type": "matn",
     "ar": "ولما كان وجود الضمير غير ظاهر في الصفة[[٣]] مثل ظهوره[[٤]] في المعمول احتيج إلى قاعدة يظهر بها وجوده وعدمه، فقال:",
     "en": "Since the presence of the pronoun is not as apparent in the adjective as its appearance in the governed term, a rule was needed by which its presence and absence become apparent; so he said:"},
    {"type": "matn",
     "ar": "(ومتى رفعت) معمول الصفة (بها فلا ضمير فيها) أي: في الصفة؛ لأن معمولها حينئذ[[٥]] فاعل لها، فلو كان فيها ضمير يلزم تعدد",
     "en": "(Whenever you put) the governed term of the adjective (in the nominative by it, there is no pronoun in it), that is, in the adjective, because its governed term is then its agent (fāʿil); so if there were a pronoun in it, a multiplicity…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: أن الضمير فيه ليس إلا للربط بدليل جواز الحسن الوجه بالجر، والحسن وجهه بالرفع.",
     "en": "He means that the pronoun in it serves only for linking, as is shown by the permissibility of “al-ḥasanu l-wajhi” with the genitive and “al-ḥasanu wajhuhu” with the nominative."},
    {"type": "pair",
     "ar": "وقد حصل الربط بأحدهما، فالثاني زائد بخلاف ما إذا جيء بالضمير، ويكون الغرض من أحدهما الربط، ومن الآخر تعيين المضاف نحو: زيد أحسن ضربه من ضرب أبيه في داره.",
     "en": "The link is achieved by one of them, so the second is superfluous; unlike when the pronoun is brought in and the purpose of one of them is linking and of the other specifying the first term of the annexation, as in “Zaydun aḥsanu ḍarbihi min ḍarbi abīhi fī dārihi” (Zayd’s beating him is better than his father’s beating in his house)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وليس اللام في الحسن الوجه وحسن وجه رابطة؛ لأن إبدال اللام من الضمير فيما يشترط فيه الضمير قبيح عند البصريين كما في الرضي.",
     "en": "The lām in “al-ḥasanu l-wajhu” and “ḥasanun wajhun” is not a link, because substituting the lām for the pronoun where the pronoun is required is ugly according to the Baṣrans, as in al-Raḍī."},
    {"type": "pair",
     "ar": "ومن هذا ظهر الفرق بينهما وبين: نعم الرجل زيد؛ لأن اللام فيه رابطة، وليست بدلا من الضمير.",
     "en": "From this the difference appears between these two and “niʿma l-rajulu Zaydun” (how excellent a man is Zayd), for the lām in it is a link and is not a substitute for the pronoun."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لكونه مستترا.",
     "en": "Because it is latent."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لكونه بارزا.",
     "en": "Because it is overt."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: حين رفعت المعمول بها فاعلا لها؛ إذ لا وجه لرفعها غير الفاعلية،",
     "en": "That is, when you put the governed term in the nominative by it as its agent, since there is no ground for its nominative other than agency;"},
    # REVIEW: printed «تعددا الفاعل» (with tanwīn-alif, printed with fatḥatān, before a definite noun); expected «تعدد الفاعل». Transcribed as printed (diacritics removed).
    {"type": "pair",
     "ar": "فلو كان فيها ضمير يكون فاعلا لعدم جواز استتار غير الفاعل للزم تعددا الفاعل",
     "en": "so if there were a pronoun in it, it would be an agent, since a non-agent cannot be latent, and a multiplicity of agents would follow."},
    {"type": "pair",
     "ar": "فما قيل: إنه يجوز أن يكون المعمول بدلا من الضمير المستتر. وهم، كما لا يخفى.",
     "en": "So what has been said, that the governed term may be a substitute (badal) for the latent pronoun, is a mistake, as is not hidden."},
]
