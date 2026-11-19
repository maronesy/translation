# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 456 (printed ٤٥٥)."""

PAGE_NUMBER = 456
PRINTED_PAGE = "٤٥٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… ولم يتنبهوا أن الاشتقاق متضمن معنى الوضع كما» at the foot of PDF p. 455 (mid-sentence).
    {"type": "matn",
     "ar": "علمت، فليس اسم التفضيل موضوعا لمن قام به، بل له مع الزيادة.",
     "en": "…you have learned; so the noun of preference is not coined for one in whom [the verb] subsists, but for him with the excess."},
    {"type": "matn",
     "ar": "ويخدشه أن صيغة المبالغة على هذا التقدير تخرج من التعريف، ولا يبعد أن يلتزم ذلك[[١]]،",
     "en": "Against this it may be objected that on this account the intensive form (ṣīghat al-mubālagha) is excluded from the definition; but it is not far-fetched to accept that,"},
    {"type": "matn",
     "ar": "ويدل عليه حصره صيغ اسم الفاعل فيما حصر، وجعل أحكام صيغ المبالغة مثل أحكام اسم الفاعل،",
     "en": "as is indicated by his confining the forms of the active participle to those to which he confined them, and his making the rules of the intensive forms like the rules of the active participle."},
    {"type": "matn",
     "ar": "وفي الترجمة الشريفة الشريفية ما معناه: أن صيغة اسم الفاعل من الثلاثي المجرد على فاعل كـ«ضارب، وقاتل، وماش وآكل»،",
     "en": "In al-Tarjama al-Sharīfa al-Sharīfiyya there is what amounts to this: the form of the active participle from the bare triliteral is on the pattern fāʿil, like “ḍārib” (striker), “qātil” (killer), “māshin” (walker) and “ākil” (eater);"},
    {"type": "matn",
     "ar": "وكل ما اشتق من مصادر الثلاثي لمن قام به لا على هذه الصيغة، فهو ليس باسم الفاعل، بل هو صفة مشبهة، أو أفعل التفضيل أو صيغة المبالغة كـ«حسن، وأحسن، ومضراب».",
     "en": "and whatever is derived from the verbal nouns of the triliteral for one in whom it subsists, not on this form, is not an active participle but a resembling adjective, an elative afʿal, or an intensive form, like “ḥasan” (handsome), “aḥsan” (more handsome) and “miḍrāb” (much-striking)."},
    {"type": "matn",
     "ar": "(وصيغته) أي: صيغة اسم الفاعل (من الثلاثي المجرد على) زنة («فاعل» ومن غيره) ثلاثيا مزيدا فيه، أو رباعيا مجردا، أو مزيدا فيه",
     "en": "(And its form), that is, the form of the active participle, (from the bare triliteral is on) the measure (“fāʿil”, and from what is other than it), whether augmented triliteral, or bare or augmented quadriliteral,"},
    {"type": "matn",
     "ar": "(على صيغة المضارع) المعلوم (بميم) أي: مع ميم (مضمومة) موضوعة في موضع حرف المضارعة سواء كان حرف المضارعة مضمومة أو لا",
     "en": "(on the form of the) active (imperfect, with a mīm), that is, together with a mīm, (with ḍamma), placed in the position of the prefix of the imperfect, whether the prefix of the imperfect has a ḍamma or not,"},
    {"type": "matn",
     "ar": "(و) مع (كسر ما قبل الآخر) وإن لم يكن فيما قبل آخر المضارع كسر، كما في «يتفعل، ويتفاعل، ويتفعلل»",
     "en": "(and) with (a kasra on the penultimate letter), even if the penultimate of the imperfect has no kasra, as in “yatafaʿʿalu”, “yatafāʿalu” and “yatafaʿlalu”,"},
    {"type": "matn",
     "ar": "(مثل: «مدخل») فيما وضع الميم موضع حرف المضارعة المضمومة (و«مستغفر») فيما وضعت موضع حرف المضارعة المفتوحة،",
     "en": "(as in “mudkhil”) (one who brings in), where the mīm is placed in the position of an imperfect prefix with ḍamma, (and “mustaghfir”) (one who seeks forgiveness), where it is placed in the position of an imperfect prefix with fatḥa."},
    {"type": "matn",
     "ar": "ولو أقيم «متفاعل» مقام «مستغفر» لكان مثال الكسر الغير الواقع في آخر المضارع أيضا مذكورا،",
     "en": "Had “mutafāʿil” been put in place of “mustaghfir”, an example of the kasra not occurring in the penultimate of the imperfect would also have been mentioned;"},
    {"type": "matn",
     "ar": "فكما يكون لكل من قسمي الميم مثال، يكون لكل من قسمي الكسر أيضا مثال.",
     "en": "so just as each of the two kinds of mīm has an example, each of the two kinds of kasra would also have an example."},
    {"type": "matn",
     "ar": "(ويعمل[[٢]]) أي: اسم الفاعل (عمل فعله) فإن كان فعله لازما يكون هو أيضا لازما، ويعمل عمل فعله اللازم،",
     "en": "(And it governs), that is, the active participle, (as its verb governs): if its verb is intransitive, it too is intransitive and governs as its intransitive verb governs;"},
    {"type": "matn",
     "ar": "وإن كان متعديا إلى مفعول واحد يكون هو أيضا متعديا إلى مفعول واحد، وإن كان متعديا إلى اثنين كان هو أيضا كذلك،",
     "en": "if it is transitive to one object, it too is transitive to one object; and if it is transitive to two, it too is likewise;"},
    {"type": "matn",
     "ar": "وكما أن فعله يتعدى إلى الظرفين، والحال، والمصدر، والمفعول له، والمفعول معه، وسائر الفضلات كذلك يتعدى هو إليها",
     "en": "and just as its verb extends to the two adverbials [of time and place], the circumstantial qualifier (ḥāl), the verbal noun, the object of purpose, the object of accompaniment and the other complements (faḍalāt), so it too extends to them,"},
    {"type": "matn",
     "ar": "(بشرط معنى الحال أو الاستقبال) أي: يعمل اسم الفاعل حال كونه متلبسا بشرط، أي: بشيء يشترط عمله به من معنى هو زمان الحال أو الاستقبال، فالإضافتان بيانيتان،",
     "en": "(on condition of the sense of the present or the future), that is, the active participle governs while joined to a condition, that is, to something on which its governing is conditional, namely a sense that is present or future time; so both annexations are explicative (bayāniyya)."},
    {"type": "matn",
     "ar": "وإنما اشترط أحدهما؛ لأن عمله لشبه المضارع،",
     "en": "One of the two is made a condition only because its governing is due to its resemblance to the imperfect,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «أي: على زمنه»; the sense requires «على زعمه» ("according to his claim"). Transcribed as printed, translated as «زعمه».
    {"type": "pair",
     "ar": "الأولى ترك لفظ البعد، فإنه قال ابن مالك في شرح التسهيل: ولزم من تقييد اسم الفاعل بكونه جاريا على المضارع أي: على زمنه خروج أمثلة المبالغة،",
     "en": "It would be better to drop the word “far-fetched”; for Ibn Mālik said in Sharḥ al-Tashīl: from restricting the active participle to what runs on the imperfect (that is, according to his claim) it follows that the intensive patterns are excluded,"},
    # REVIEW: printed «ولم يكن في ذلك ضمير» ("pronoun"); the sense requires «ضير» ("harm"). Transcribed as printed, translated as «ضير».
    {"type": "pair",
     "ar": "ولم يكن في ذلك ضمير؛ لأن اسم الفاعل غيرها.",
     "en": "and there was no harm in that, because the active participle is other than them."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيد في التسهيل بغير المصغر والموصوف خلافا للكسائي، فإنه جوز عمل المصغر والموصوف.",
     "en": "In al-Tashīl it is restricted to what is neither diminutive nor qualified, against al-Kisāʾī, for he permitted the diminutive and the qualified to govern."},
]
