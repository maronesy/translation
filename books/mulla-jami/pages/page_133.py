# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 133 (printed ١٣٢)."""

PAGE_NUMBER = 133
PRINTED_PAGE = "١٣٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "ذلك[[١]] إسكان اللام في «ضربت»؛ لأنه لدفع توالي أربع حركات فيما هو بمنزلة كلمة واحدة.",
     "en": "that [i.e.] the making of the lām quiescent in “ḍarabtu”; because it serves to ward off the succession of four consecutive vowels in what stands in the position of a single word."},
    {"type": "matn",
     "ar": "(فلذلك[[٢]]) الأصل الذي يقتضي تقديم الفاعل على سائر معمولات الفعل (جاز «ضرب غلامه زيد») لتقدم مرجع الضمير، وهو «زيد» رتبة[[٣]]، فلا يلزم الإضمار قبل الذكر مطلقا، بل لفظا فقط، وذلك جائز[[٤]].",
     "en": "(So on that account) — [namely] the principle that requires the priority of the agent (fāʿil) over all the other governed elements of the verb — (it is permissible [to say] “ḍaraba ghulāmuhu Zayd,” “his slave-boy struck Zayd”), because the antecedent of the pronoun, which is “Zayd,” precedes [it] in rank; so pronominalization before the [explicit] mention is not entailed absolutely, but only verbally, and that is permissible."},
    {"type": "matn",
     "ar": "(وامتنع: «ضرب غلامه زيدا») لتأخر مرجع الضمير، وهو «زيد» لفظا ورتبة، فيلزم الإضمار قبل الذكر لفظا ورتبة، وذلك غير جائز، خلافا للأخفش وابن جني[[٥]]،",
     "en": "(And it is precluded [to say]: “ḍaraba ghulāmuhu Zaydan,” “his slave-boy struck Zayd [accusative]”), because the antecedent of the pronoun, which is “Zayd,” comes later both verbally and in rank; so pronominalization before the [explicit] mention is entailed both verbally and in rank, and that is impermissible — contrary to al-Akhfash and Ibn Jinnī,"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "دلالة «إن» كما أن السابق دل عليه دلالة «لم». ويدل أيضا تلك الدلالة وضع إعراب الفعل بعد الفاعل، نحو: يضربان، ويضربون، وتضربين.",
     "en": "the signification of “in” [as a jussive particle], just as what preceded was indicated by the signification of “lam.” That same signification is also indicated by the placement of the verb’s inflection after the agent, as in yaḍribāni, yaḍribūna, and taḍribīna."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "اللام للتعليل يفيد أن كون الولي أصلا علة لجواز المثال الأول وامتناع الثاني.",
     "en": "The lām [in “fa-li-dhālika”] is for causation, conveying that the antecedent’s being a foundation is the cause of the permissibility of the first example and the impermissibility of the second."},
    {"type": "pair",
     "ar": "والفاء إما للتفريع، فتفيد ترتيب العلم بالجواز والامتناع فيهما على العلم بالأصل السابق، أو للتعليل، فيكون من باب الاستدلال بالمعلول على العلة.",
     "en": "The fāʾ is either for sequential derivation (tafrīʿ), thus conveying that knowledge of the permissibility and impermissibility in the two [examples] is ordered upon knowledge of the foregoing principle; or it is for causation, in which case it belongs to the category of inferring the cause from the effect."},
    {"type": "pair",
     "ar": "فلا استدراك في الجمع بين الفاء واللام.",
     "en": "So there is no redundancy in combining the fāʾ and the lām."},
    {"type": "pair",
     "ar": "ولا يخفى أن امتناع المثال المذكور وإن كان يترتب على الأصل المذكور، لكنه لا يتوقف عليه لثبوته على تقدير تساويهما في المرتبة، فلا يصح الاستدلال بالامتناع عليه.",
     "en": "It is not hidden that the impermissibility of the said example, though it follows upon the said principle, does not depend on it — since it would still hold even on the supposition of their being equal in rank — so it is not valid to infer that [principle] from the impermissibility."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "تقدم الشيء على أمر رتبة: كون الشيء بحالة مقتضية للتقدم سواء تقدم بالفعل أو لم يتقدم، وهو حينئذ في حكم المتقدم؛ لأن ثبوت السبب في قوة ثبوت المسبب، فيكون من قبيل وضع السبب موضع المسبب.",
     "en": "The priority of a thing over some matter in rank is: the thing’s being in a state that requires priority, whether it actually precedes or not; and it is then treated as though it precedes, because the establishment of the cause is tantamount to the establishment of the effect, so it is of the sort of putting the cause in the place of the effect."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: عند الجمهور. والأولى جوازه لوروده في كلام الفصحاء.",
     "en": "That is: according to the majority. The preferable [view] is that it is permissible, because of its occurrence in the speech of the eloquent Arabs."},
    {"type": "pair",
     "ar": "وقد حصر بعضهم مواضع الإضمار قبل الذكر في سبعة: أحدها: أن يكون الضمير مرفوعا بنعم وبئس وبابهما، ولا يفسره إلا التمييز، نحو: نعم رجلا زيد.",
     "en": "Some have confined the instances of pronominalization before the [explicit] mention to seven: The first: that the pronoun be nominative by virtue of niʿma, biʾsa, and their class, and that only the specification (tamyīz) explains it, as in niʿma rajulan Zayd (“What an excellent man Zayd is!”)."},
    {"type": "pair",
     "ar": "ثانيها: أن يكون مرفوعا بأول المتنازعين والمهمل ثانيهما.",
     "en": "The second: that it be nominative by virtue of the first of two governors in a construction of mutual government (tanāzuʿ), the neglected one being the second of them."},
    {"type": "pair",
     "ar": "ثالثها: أن يكون مخبرا عنه، ومفسره خبره، نحو:",
     "en": "The third: that it be the subject of a predication, its explainer being its predicate, as in:"},
    {"type": "quran",
     "ar": "﴿وقالوا إن هي إلا حياتنا الدنيا وما نحن بمبعوثين﴾ (سورة الأنعام:٢٩)",
     "en": "“And they said: There is nothing but our life in this world, and we shall not be raised again” (Qurʾān, Sūrat al-Anʿām 6:29),"},
    {"type": "pair",
     "ar": "أي: إن الحياة إلا حياتنا الدنيا، ثم وضع «هي» موضع «الحياة»؛ لأن الخبر يدل عليها ويبينها.",
     "en": "that is: “there is no life but our life in this world,” and then “hiya” (it/she) was put in the place of “life,” because the predicate indicates it and clarifies it."},
    {"type": "pair",
     "ar": "رابعها: ضمير الشأن والقصة، نحو:",
     "en": "The fourth: the pronoun of the matter or the affair (ḍamīr al-shaʾn wa-l-qiṣṣa), as in:"},
    {"type": "quran",
     "ar": "﴿قل هو الله أحد﴾ (سورة الإخلاص:١)، ﴿فإذا هي شاخصة﴾ (سورة الأنبياء:٩٧)",
     "en": "“Say: He, Allah, is One” (Qurʾān, Sūrat al-Ikhlāṣ 112:1); “and lo, they are staring” (Qurʾān, Sūrat al-Anbiyāʾ 21:97)."},
    {"type": "pair",
     "ar": "خامسها: أن يجر بـ«رب»، ويفسره التمييز، نحو: «ربه رجلا».",
     "en": "The fifth: that it be in the genitive by virtue of “rubba,” with the specification explaining it, as in rubbahu rajulan (“many a man he is!”)."},
    {"type": "pair",
     "ar": "سادسها: أن يكون أبدلت عنه مرجعه، فكان مفسرا له، نحو: «ضربته زيدا»، وقولهم: اللهم صل عليه الرؤوف الرحيم.",
     "en": "The sixth: that its antecedent be substituted for it, so that it becomes its explainer, as in ḍarabtuhu Zaydan (“I struck him, Zayd”), and their saying: “O Allah, bless him, the Compassionate, the Merciful.”"},
    {"type": "pair",
     "ar": "سابعها: أن يكون متصلا بفاعل مقدم يفسره مفعول مؤخر كضرب غلامه زيدا، كذا في شذور الذهب.",
     "en": "The seventh: that it be attached to a preceding agent that a following object explains, as in ḍaraba ghulāmuhu Zaydan; thus [it is stated] in Shudhūr al-Dhahab."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بسكون الياء. فإنهما جوزا اتصال ضمير المفعول به بالفاعل مع تقدم الفاعل لشدة اقتضاء الفعل للمفعول به كاقتضاء الفاعل.",
     "en": "[Ibn] Jinnī, with a quiescent yāʾ. For the two of them permitted the attaching of the pronoun of the object (mafʿūl bihi) to the agent, together with the agent’s precedence, on account of the strength of the verb’s requiring the object, like its requiring the agent."},
    {"type": "pair",
     "ar": "وفيه أنه لا يقتضي تقديمه على الفاعل، نعم يستدعي تقدمه على ما سوى الفاعل.",
     "en": "But against this [it may be said] that it does not require its precedence over the agent; yes, it does call for its precedence over what is other than the agent."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: الأولى تجويز ذلك، وليس للبصرية المنع مع قولهم في باب التنازع، انتهى.",
     "en": "Shaykh al-Raḍī said: The preferable [view] is to permit that, and the Basrans have no [right] to forbid it given what they say in the chapter on tanāzuʿ. End [of quotation]."},
    {"type": "pair",
     "ar": "قيل: تجويز الإضمار قبل الذكر في باب التنازع في العمدة، والضمير المضاف إليه غير عمدة.",
     "en": "It has been said: the permitting of pronominalization before the [explicit] mention in the chapter on tanāzuʿ concerns a principal element (ʿumda), whereas the pronoun to which [a noun] is annexed is not a principal element."},
    {"type": "pair",
     "ar": "وقيل: تجويزه للضرورة؛ إذ لو لم يضمر لزم إما حذف الفاعل، وهو غير جائز، أو التكرار وهو قبيح،",
     "en": "And it has been said: it is permitted out of necessity; for if no pronoun were used, there would follow either the deletion of the agent — which is impermissible — or repetition, which is unseemly,"},
    {"type": "pair",
     "ar": "وفيه أن ارتكاب القبيح أهون من ارتكاب الممتنع مع أن مثل ما ذكره جار هنا؛ لأن حذف المضاف",
     "en": "but against this [it may be said] that committing what is unseemly is easier to bear than committing what is impossible; moreover, the like of what he mentioned applies here [too], because the deletion of the annexed noun (muḍāf)"},
]
